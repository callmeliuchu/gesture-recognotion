using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using AForge.Video;
using AForge.Imaging;
using AForge.Math;
using System.Drawing.Imaging;
using AForge.Video.DirectShow;
using System.IO;
using Baidu.Aip.Speech;
using System.Net;
using System.Web;
using Newtonsoft.Json.Linq;
using System.Runtime.InteropServices;

namespace Gesture_Recognition
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        static readonly String APP_ID = "26039766";
        static readonly String APP_KEY = "VYV5AEU9ljKsUUjFSdlZVElS";
        static readonly String SECRET_KEY = "HFdiKGhdAnsaei45NDpgGpPa9Gkns2bz";

        readonly Tts ttsClient = new Baidu.Aip.Speech.Tts(APP_KEY, SECRET_KEY);
        [DllImport("winmm.dll", SetLastError = true)]
        private static extern long mciSendString(string strCommand, StringBuilder strReturn, int iReturnLength, IntPtr hwndCallback);
        private FilterInfoCollection videoDevices;
        private VideoCaptureDevice videoDevice;
        String imgBase64;
        private void Form1_Load(object sender, EventArgs e)
        {
            videoDevices = new FilterInfoCollection(FilterCategory.VideoInputDevice);
            if (videoDevices.Count != 0)
            {
                foreach (FilterInfo device in videoDevices)
                {
                    cmbCamera.Items.Add(device.Name);
                }
            }
            else
            {
                openCamera.Enabled = false;
                closeCamera.Enabled = false;
                cmbCamera.Items.Add("没有找到摄像头");
            }

            cmbCamera.SelectedIndex = 0;
        }
        private void openCamera_Click(object sender, EventArgs e)
        {
            if (videoDevice != null)
            {
                openCamera.Enabled = false;
                closeCamera.Enabled = true;
                btnShoot.Enabled = true;
                openPictureBtn.Enabled = true;
                vispShoot.VideoSource = videoDevice;
                vispShoot.Start();


            }
        }

        private void closeCamera_Click(object sender, EventArgs e)
        {
            if (vispShoot.VideoSource != null)
            {
                vispShoot.SignalToStop();
                vispShoot.WaitForStop();
                vispShoot.VideoSource = null;
                openCamera.Enabled = true;
                closeCamera.Enabled = false;
                btnShoot.Enabled = false;
                discernBtn.Enabled = false;
                openPictureBtn.Enabled=false;
            }
        }

        private void cmbCamera_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (videoDevices.Count != 0)
            {
                videoDevice = new VideoCaptureDevice(videoDevices[cmbCamera.SelectedIndex].MonikerString);
            }
        }

        private void btnShoot_Click(object sender, EventArgs e)
        {

            Bitmap img = vispShoot.GetCurrentVideoFrame();
            imgBase64 = ImgToBase64String(img);
            pictureBox1.Image = img;
            discernBtn.Enabled = true;
        }

        private void discernBtn_Click(object sender, EventArgs e)
        {

            String numStr = discernNum();
            label3.Text = numStr;

            String resultString = numStr == "0" ? "所有灯都关了" : String.Format("共有{0}个灯亮了", numStr);

            // 可选参数
            var option = new Dictionary<string, object>()
            {
                {"spd", 5}, // 语速
                {"vol", 7}, // 音量
                {"per", 4}  // 发音人，4：情感度丫丫童声
            };

            var result = ttsClient.Synthesis(resultString, option);
            if (result.ErrorCode == 0)  // 或 result.Success
            {
                // 保存结果为mp3格式
                File.WriteAllBytes("temp.mp3", result.Data);
                // 播放音频文件
                mciSendString("open temp.mp3 alias temp_alias", null, 0, IntPtr.Zero);
                mciSendString("play temp_alias", null, 0, IntPtr.Zero);
                // 等待播放结束
                StringBuilder strReturn = new StringBuilder(64);
                do
                {
                    mciSendString("status temp_alias mode", strReturn, 64, IntPtr.Zero);
                } while (!strReturn.ToString().Contains("stopped"));
                // 关闭音频文件
                mciSendString("close temp_alias", null, 0, IntPtr.Zero);

            }
            else
            {
                MessageBox.Show("语音合成失败：" + result.ErrorMsg);
            }
        }

        private String discernNum()
        {

            string host = "http://106.14.149.194:8080/command";
            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(host);
            request.Method = "post";
            request.ContentType = "application/json";
            request.KeepAlive = true;
            // 图片的base64编码
            String str = "{\"image\":\"" + imgBase64 + "\"}";
            byte[] buffer = UTF8Encoding.UTF8.GetBytes(str);
            request.ContentLength = buffer.Length;
            request.GetRequestStream().Write(buffer, 0, buffer.Length);
            HttpWebResponse response = (HttpWebResponse)request.GetResponse();
            StreamReader reader = new StreamReader(response.GetResponseStream(), Encoding.Default);
            string result = reader.ReadToEnd();
            Console.WriteLine("检测数字");
            JObject jResult = JObject.Parse(result);
            if (jResult != null && jResult["code"].ToString() == "200")
            {
                return jResult["data"]["predict"].ToString();
            }
            else
            {
                MessageBox.Show("检测数字API出错");
                return "";
            }
        }

        public string ImgToBase64String(Bitmap bmp)
        {
            try
            {
                MemoryStream ms = new MemoryStream();
                bmp.Save(ms, System.Drawing.Imaging.ImageFormat.Jpeg);
                byte[] arr = new byte[ms.Length];
                ms.Position = 0;
                ms.Read(arr, 0, (int)ms.Length);
                ms.Close();
                return Convert.ToBase64String(arr);
            }
            catch (Exception ex)
            {
                return null;
            }
        }

        private void openPictureBtn_Click(object sender, EventArgs e)
        {
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                // 填充 文件路径 & 格式
                String imgPath = openFileDialog1.FileName;
                imgBase64 = Convert.ToBase64String(File.ReadAllBytes(imgPath));
                pictureBox1.Image = System.Drawing.Image.FromFile(imgPath);
                discernBtn.Enabled = true;
            }
            else
            {
                MessageBox.Show("访问图片出错");
            }
        }
    }
}
