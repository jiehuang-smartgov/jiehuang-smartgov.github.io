# 黄婕个人学术主页 al-folio 上传包

这个包是为已经下载的 `alshedivat/al-folio` 模板准备的内容覆盖包。它不会包含原始简历 PDF，也没有公开手机号、出生年月、籍贯、政治面貌等私人信息。

## 推荐使用方式

1. 备份你的 al-folio 文件夹。
2. 解压本 zip 到 al-folio 根目录，也就是能看到 `_config.yml`、`_pages/`、`_bibliography/`、`assets/` 的那一层。
3. 允许覆盖同名文件。
4. 在 al-folio 根目录运行：

```bash
python apply_huangjie_site.py
```

5. 按提示输入你的 GitHub 用户名，例如：

```text
jiehuang-ruc
```

脚本会自动把 `_config.yml` 中的网站姓名、标题、邮箱、简介、关键词、网址、Jekyll Scholar 作者高亮等字段改成黄婕主页版本，并保留 al-folio 模板的其它技术配置。

## 如果不运行脚本，至少手动修改 `_config.yml`

请在 `_config.yml` 中确认以下字段：

```yaml
title: "Jie Huang | 黄婕"
first_name: "Jie"
middle_name: ""
last_name: "Huang"
email: "huangjie2018@ruc.edu.cn"
url: "https://你的GitHub用户名.github.io"
baseurl: ""
description: "Jie Huang is a Lecturer at the School of Smart Governance, Renmin University of China. Her research focuses on smart governance, public data governance, data standardization, semantic interoperability, and AI data governance."
keywords: smart governance, public data governance, data standardization, semantic interoperability, AI data governance, smart cities, information resource management
lang: en
```

并把 `scholar` 部分中的作者姓名改为：

```yaml
scholar:
  last_name: [Huang, 黄]
  first_name: [Jie, 婕]
```

## 本包主要文件

```text
_pages/about.md              首页
_pages/research.md           研究方向
_pages/publications.md       学术成果页，读取 _bibliography/papers.bib
_pages/standards.md          标准项目页
_pages/projects.md           科研项目页
_pages/teaching.md           教学页
_pages/service.md            学术服务页
_pages/awards.md             奖励页
_pages/cv.md                 在线 CV 页
_pages/contact.md            联系方式页
_bibliography/papers.bib     论文、会议论文、专著 BibTeX 数据
assets/img/prof_pic.jpg      主页头像
assets/pdf/Huang_Jie_CV_public.pdf  公开版 CV PDF
apply_huangjie_site.py       自动修正 _config.yml 的脚本
```

## 上传 GitHub

运行脚本并确认页面内容后，在 al-folio 根目录提交：

```bash
git add .
git commit -m "Build Jie Huang academic homepage"
git push
```

GitHub Actions 完成后，到仓库 `Settings -> Pages` 确认发布分支为 `gh-pages`。如果你的仓库名是 `你的GitHub用户名.github.io`，主页地址通常是：

```text
https://你的GitHub用户名.github.io
```
