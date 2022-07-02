namespace Gesture_Recognition
{
    partial class Form1
    {
        /// <summary>
        /// 必需的设计器变量。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清理所有正在使用的资源。
        /// </summary>
        /// <param name="disposing">如果应释放托管资源，为 true；否则为 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows 窗体设计器生成的代码

        /// <summary>
        /// 设计器支持所需的方法 - 不要修改
        /// 使用代码编辑器修改此方法的内容。
        /// </summary>
        private void InitializeComponent()
        {
            this.label1 = new System.Windows.Forms.Label();
            this.vispShoot = new AForge.Controls.VideoSourcePlayer();
            this.cmbCamera = new System.Windows.Forms.ComboBox();
            this.openCamera = new System.Windows.Forms.Button();
            this.closeCamera = new System.Windows.Forms.Button();
            this.pictureBox1 = new AForge.Controls.PictureBox();
            this.btnShoot = new System.Windows.Forms.Button();
            this.discernBtn = new System.Windows.Forms.Button();
            this.videoSourcePlayer1 = new AForge.Controls.VideoSourcePlayer();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.openPictureBtn = new System.Windows.Forms.Button();
            this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(13, 20);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(67, 15);
            this.label1.TabIndex = 0;
            this.label1.Text = "摄像头：";
            // 
            // vispShoot
            // 
            this.vispShoot.Location = new System.Drawing.Point(12, 88);
            this.vispShoot.Name = "vispShoot";
            this.vispShoot.Size = new System.Drawing.Size(349, 223);
            this.vispShoot.TabIndex = 1;
            this.vispShoot.Text = "videoSourcePlayer1";
            this.vispShoot.VideoSource = null;
            // 
            // cmbCamera
            // 
            this.cmbCamera.FormattingEnabled = true;
            this.cmbCamera.Location = new System.Drawing.Point(86, 17);
            this.cmbCamera.Name = "cmbCamera";
            this.cmbCamera.Size = new System.Drawing.Size(159, 23);
            this.cmbCamera.TabIndex = 2;
            this.cmbCamera.SelectedIndexChanged += new System.EventHandler(this.cmbCamera_SelectedIndexChanged);
            // 
            // openCamera
            // 
            this.openCamera.Location = new System.Drawing.Point(251, 12);
            this.openCamera.Name = "openCamera";
            this.openCamera.Size = new System.Drawing.Size(99, 34);
            this.openCamera.TabIndex = 3;
            this.openCamera.Text = "打开摄像头";
            this.openCamera.UseVisualStyleBackColor = true;
            this.openCamera.Click += new System.EventHandler(this.openCamera_Click);
            // 
            // closeCamera
            // 
            this.closeCamera.Enabled = false;
            this.closeCamera.Location = new System.Drawing.Point(355, 12);
            this.closeCamera.Name = "closeCamera";
            this.closeCamera.Size = new System.Drawing.Size(98, 34);
            this.closeCamera.TabIndex = 4;
            this.closeCamera.Text = "关闭摄像头";
            this.closeCamera.UseVisualStyleBackColor = true;
            this.closeCamera.Click += new System.EventHandler(this.closeCamera_Click);
            // 
            // pictureBox1
            // 
            this.pictureBox1.Image = null;
            this.pictureBox1.Location = new System.Drawing.Point(388, 88);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(339, 223);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.pictureBox1.TabIndex = 5;
            this.pictureBox1.TabStop = false;
            // 
            // btnShoot
            // 
            this.btnShoot.Enabled = false;
            this.btnShoot.Location = new System.Drawing.Point(564, 12);
            this.btnShoot.Name = "btnShoot";
            this.btnShoot.Size = new System.Drawing.Size(99, 34);
            this.btnShoot.TabIndex = 6;
            this.btnShoot.Text = "拍照";
            this.btnShoot.UseVisualStyleBackColor = true;
            this.btnShoot.Click += new System.EventHandler(this.btnShoot_Click);
            // 
            // discernBtn
            // 
            this.discernBtn.Enabled = false;
            this.discernBtn.Location = new System.Drawing.Point(670, 12);
            this.discernBtn.Name = "discernBtn";
            this.discernBtn.Size = new System.Drawing.Size(99, 34);
            this.discernBtn.TabIndex = 7;
            this.discernBtn.Text = "图像识别";
            this.discernBtn.UseVisualStyleBackColor = true;
            this.discernBtn.Click += new System.EventHandler(this.discernBtn_Click);
            // 
            // videoSourcePlayer1
            // 
            this.videoSourcePlayer1.Location = new System.Drawing.Point(762, 76);
            this.videoSourcePlayer1.Name = "videoSourcePlayer1";
            this.videoSourcePlayer1.Size = new System.Drawing.Size(8, 8);
            this.videoSourcePlayer1.TabIndex = 8;
            this.videoSourcePlayer1.Text = "videoSourcePlayer1";
            this.videoSourcePlayer1.VideoSource = null;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(174, 374);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(90, 15);
            this.label2.TabIndex = 9;
            this.label2.Text = "检测结果为:";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(271, 374);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(0, 15);
            this.label3.TabIndex = 10;
            // 
            // openPictureBtn
            // 
            this.openPictureBtn.Enabled = false;
            this.openPictureBtn.Location = new System.Drawing.Point(459, 12);
            this.openPictureBtn.Name = "openPictureBtn";
            this.openPictureBtn.Size = new System.Drawing.Size(99, 34);
            this.openPictureBtn.TabIndex = 11;
            this.openPictureBtn.Text = "上传图片";
            this.openPictureBtn.UseVisualStyleBackColor = true;
            this.openPictureBtn.Click += new System.EventHandler(this.openPictureBtn_Click);
            // 
            // openFileDialog1
            // 
            this.openFileDialog1.FileName = "openFileDialog1";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.openPictureBtn);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.videoSourcePlayer1);
            this.Controls.Add(this.discernBtn);
            this.Controls.Add(this.btnShoot);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.closeCamera);
            this.Controls.Add(this.openCamera);
            this.Controls.Add(this.cmbCamera);
            this.Controls.Add(this.vispShoot);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private AForge.Controls.VideoSourcePlayer vispShoot;
        private System.Windows.Forms.ComboBox cmbCamera;
        private System.Windows.Forms.Button openCamera;
        private System.Windows.Forms.Button closeCamera;
        private AForge.Controls.PictureBox pictureBox1;
        private System.Windows.Forms.Button btnShoot;
        private System.Windows.Forms.Button discernBtn;
        private AForge.Controls.VideoSourcePlayer videoSourcePlayer1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Button openPictureBtn;
        private System.Windows.Forms.OpenFileDialog openFileDialog1;
    }
}

