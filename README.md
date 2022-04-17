# RPA-Backend

## 贡献代码

除生产环境所需依赖外，本项目的开发环境还需安装如下依赖

### 文档

文档放置在[`./docs`](docs)文件夹中，本项目使用[`mkdocs`](https://www.mkdocs.org/getting-started/)自动编译文档，并使用[`mkdocs-material`](<https://squidfunk.github.io/mkdocs-material/getting-started/>)主题和[`mkdocstrings`](https://mkdocstrings.github.io/)从Python文件生成文档，所以在构建文档之前需要先安装以上依赖

```bash
pip install mkdocs mkdocs-material mkdocstrings
```

#### 文档开启本机服务

```bash
mkdocs serve
```

#### 编译文档

```bash
mkdocs build
```

#### 从Python注释生成文档

在markdown文件中加入，更多用法详见[Usage](https://mkdocstrings.github.io/usage/)

```markdown
::: my_library.my_module.my_class
```
