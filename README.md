# Brother集团企业官网

这是一个基于Python Flask框架构建的现代化企业展示网站，专为Brother集团设计。

## 项目特点

- 🎨 **现代化设计** - 采用Bootstrap 5和响应式设计
- 📱 **移动端友好** - 完美适配各种设备
- 🚀 **快速加载** - 优化的代码结构和资源加载
- 🔧 **易于维护** - 清晰的代码结构和模块化设计
- 🌐 **多语言支持** - 支持中文界面

## 功能模块

### 主要页面
- **首页** - 公司简介、核心业务展示
- **关于我们** - 公司背景、团队介绍、企业价值观
- **服务项目** - 详细的服务内容展示
- **产品展示** - 各类产品图片和介绍
- **新闻动态** - 公司新闻和行业资讯
- **联系我们** - 联系表单和联系信息

### 核心功能
- 响应式导航菜单
- 联系表单处理
- 产品分类筛选
- 新闻展示
- 社交媒体链接
- 常见问题解答

## 技术栈

- **后端框架**: Python Flask
- **数据库**: SQLite (可扩展至MySQL/PostgreSQL)
- **前端框架**: Bootstrap 5
- **图标库**: Font Awesome
- **字体**: Google Fonts (Noto Sans SC)

## 安装和运行

### 环境要求
- Python 3.7+
- pip

### 安装步骤

1. **克隆项目**
```bash
git clone <项目地址>
cd brother-website
```

2. **创建虚拟环境**
```bash
python -m venv venv
```

3. **激活虚拟环境**
```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

4. **安装依赖**
```bash
pip install -r requirements.txt
```

5. **运行应用**
```bash
python app.py
```

6. **访问网站**
打开浏览器访问: http://localhost:5000

## 项目结构

```
brother-website/
├── app.py                 # Flask应用主文件
├── requirements.txt       # Python依赖包
├── README.md             # 项目说明文档
├── templates/            # HTML模板文件
│   ├── base.html         # 基础模板
│   ├── index.html        # 首页
│   ├── about.html        # 关于我们
│   ├── services.html     # 服务项目
│   ├── products.html     # 产品展示
│   ├── news.html         # 新闻动态
│   └── contact.html      # 联系我们
└── static/               # 静态资源文件
    ├── css/              # CSS样式文件
    ├── js/               # JavaScript文件
    └── images/           # 图片资源
```

## 配置说明

### 数据库配置
项目使用SQLite数据库，数据库文件会自动创建在项目根目录下。

### 邮件配置
如需启用邮件功能，请在`app.py`中配置SMTP设置：

```python
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your-password'
```

## 自定义配置

### 修改公司信息
在`templates/base.html`中修改：
- 公司名称
- 联系方式
- 地址信息
- 社交媒体链接

### 修改样式
在`templates/base.html`的`<style>`标签中修改CSS变量：
```css
:root {
    --primary-color: #1e3a8a;    /* 主色调 */
    --secondary-color: #3b82f6;  /* 次要色调 */
    --accent-color: #f59e0b;     /* 强调色 */
}
```

### 添加新页面
1. 在`templates/`目录下创建新的HTML模板
2. 在`app.py`中添加对应的路由
3. 在导航菜单中添加链接

## 部署说明

### 生产环境部署
1. 使用Gunicorn作为WSGI服务器
2. 配置Nginx作为反向代理
3. 设置环境变量
4. 配置SSL证书

### Docker部署
```bash
# 构建镜像
docker build -t brother-website .

# 运行容器
docker run -p 5000:5000 brother-website
```

## 维护和更新

### 定期维护
- 更新依赖包版本
- 检查安全漏洞
- 备份数据库
- 监控网站性能

### 内容更新
- 新闻动态：在数据库中更新新闻内容
- 产品信息：修改产品展示页面
- 服务内容：更新服务项目页面

## 技术支持

如有技术问题，请联系开发团队或提交Issue。

## 许可证

本项目仅供Brother集团内部使用。

---

**Brother集团** - 专业转运服务与贸易解决方案提供商 