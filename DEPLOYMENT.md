# 部署到Vercel免费服务器

## 步骤1：安装Vercel CLI
```bash
npm install -g vercel
```

## 步骤2：登录Vercel
```bash
vercel login
```

## 步骤3：部署项目
```bash
vercel
```

## 步骤4：设置环境变量（可选）
如果需要数据库或其他配置，可以在Vercel控制台设置环境变量。

## 步骤5：自动部署
每次推送到GitHub时，Vercel会自动重新部署。

## 注意事项
- 确保所有依赖都在requirements.txt中
- SQLite数据库在Vercel上是只读的，生产环境建议使用PostgreSQL
- 静态文件会自动处理 