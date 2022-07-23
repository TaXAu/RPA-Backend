from src.parser.parser import run_program_from_file as rpa_run

## 从JSON文件中读取动作流并运行

# 第一个例子，打开百度搜索关键词
# rpa_run("src/tests/test1.json")

# 第二个例子，打开测试网站自动填写表单
rpa_run("src/tests/test2.json")

## 由于使用WebDriver的方式，所以一般的干扰不会出现问题
