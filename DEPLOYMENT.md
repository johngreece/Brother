# Brother集团网站部署指南

## 免费服务器部署选项

### 1. Vercel (推荐)

#### 步骤：
1. **注册Vercel账户**
   - 访问 https://vercel.com
   - 使用GitHub账户注册

2. **上传代码到GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/brother-website.git
   git push -u origin main
   ```

3. **在Vercel中导入项目**
   - 登录Vercel
   - 点击"New Project"
   - 选择您的GitHub仓库
   - 点击"Deploy"

4. **配置自定义域名**
   - 在项目设置中添加域名：www.brotherike.com
   - 配置DNS记录（需要域名提供商支持）

### 2. Railway

#### 步骤：
1. **注册Railway账户**
   - 访问 https://railway.app
   - 使用GitHub账户注册

2. **创建新项目**
   - 点击"New Project"
   - 选择"Deploy from GitHub repo"
   - 选择您的仓库

3. **配置环境变量**
   - 添加必要的环境变量

4. **部署**
   - Railway会自动检测Python项目并部署

### 3. Render

#### 步骤：
1. **注册Render账户**
   - 访问 https://render.com
   - 使用GitHub账户注册

2. **创建Web Service**
   - 点击"New +"
   - 选择"Web Service"
   - 连接GitHub仓库

3. **配置部署设置**
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`

4. **部署**
   - 点击"Create Web Service"

## 域名配置

### 配置www.brotherike.com

1. **购买域名**（如果还没有）
   - 推荐：Namecheap, GoDaddy, 阿里云

2. **配置DNS记录**
   ```
   Type: CNAME
   Name: www
   Value: your-app.vercel.app (或您的服务器地址)
   ```

3. **在服务器平台添加域名**
   - 在Vercel/Railway/Render中添加自定义域名
   - 验证域名所有权

## 部署检查清单

- [ ] 代码已上传到GitHub
- [ ] 服务器平台账户已注册
- [ ] 项目已导入到服务器平台
- [ ] 域名已配置
- [ ] SSL证书已激活
- [ ] 网站可以正常访问

## 维护建议

1. **定期备份**
   - 定期备份代码和数据库

2. **监控性能**
   - 使用服务器平台提供的监控工具

3. **更新依赖**
   - 定期更新Python包版本

4. **安全更新**
   - 及时更新安全补丁

## 技术支持

如遇到部署问题，请检查：
- 代码语法是否正确
- 依赖包是否完整
- 环境变量是否配置正确
- 域名DNS是否正确配置 