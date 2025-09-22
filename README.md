# 上海慧引智能科技有限公司官方网站

基于 Flask 开发的企业官方网站，用于 ICP 备案审核。

## 项目结构

```
homepage/
├── app.py              # Flask 主应用文件
├── requirements.txt    # Python 依赖包
├── README.md          # 项目说明文档
├── templates/         # HTML 模板目录
│   ├── base.html      # 基础模板
│   ├── index.html     # 首页
│   ├── about.html     # 关于我们
│   ├── services.html  # 服务页面
│   └── contact.html   # 联系我们
└── static/           # 静态文件目录
    ├── css/
    │   └── style.css  # 样式文件
    └── js/
        └── main.js    # JavaScript 文件
```

## 本地开发环境设置

### 1. 创建虚拟环境

```bash
# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
# macOS/Linux:
source venv/bin/activate
# Windows:
# venv\Scripts\activate
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 运行开发服务器

```bash
python app.py
```

网站将在 `http://localhost:8080` 启动。

### 4. 访问页面

- 首页: http://localhost:8080/
- 关于我们: http://localhost:8080/about
- 服务: http://localhost:8080/services
- 联系我们: http://localhost:8080/contact

## 生产环境部署

### 使用 Gunicorn 运行

```bash
# 安装 gunicorn (已包含在 requirements.txt 中)
pip install gunicorn

# 运行生产服务器
gunicorn -w 4 -b 0.0.0.0:8080 app:app
```

### ECS 部署步骤

1. **上传代码到服务器**
```bash
git clone <repository-url>
cd homepage
```

2. **设置 Python 环境**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. **运行服务**
```bash
# 开发环境测试 (内部访问 8080 端口)
python app.py

# 生产环境 (使用 gunicorn)
gunicorn -w 4 -b 0.0.0.0:8080 app:app

# 后台运行
nohup gunicorn -w 4 -b 0.0.0.0:8080 app:app &
```

4. **配置防火墙**
```bash
# 临时开放 80 和 443 端口用于审核
sudo ufw allow 80
sudo ufw allow 443

# 内部测试使用 8080 端口
sudo ufw allow 8080
```

## 网站特性

- **响应式设计**: 适配桌面和移动设备
- **SEO 优化**: 包含完整的 meta 标签和结构化数据
- **企业风格**: 参考 Schindler 网站的简洁专业设计
- **完整内容**: 包含公司信息、服务介绍、联系方式等

## 公司信息

- **公司名称**: 上海慧引智能科技有限公司
- **成立日期**: 2025年08月07日
- **业务范围**: 中国 & 日本
- **注册地址**: 上海市嘉定区菊园新区环城路2222号6幢101室J

## 技术栈

- **后端**: Flask (Python)
- **前端**: HTML5, CSS3, JavaScript
- **字体**: Noto Sans SC (中文优化)
- **部署**: Gunicorn + Nginx (推荐)

## 注意事项

- 确保服务器已安装 Python 3.7+
- 生产环境建议使用 Nginx 作为反向代理
- 定期更新依赖包以确保安全性
- 备案期间保持网站正常访问

## 维护

如需修改内容，请编辑对应的 HTML 模板文件。样式修改请编辑 `static/css/style.css` 文件。
