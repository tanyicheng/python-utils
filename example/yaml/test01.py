import yaml
import os


class YamlTest:

    def read(self):
        # 由于官方提示load方法存在安全漏洞，所以读取文件时会报错。加上warning忽略，就不会显示警告
        yaml.warnings({'YAMLLoadWarning': False})

        # 打开文件
        f = open('config.yaml', 'r', encoding='utf-8')
        # 读取
        cfg = f.read()
        # 将数据转换成python字典行驶输出，存在多个文件时，用load_all，单个的时候load就可以
        d = yaml.load(cfg)
        print(d)
        print(d.get('user'))
        print(d.get('job')[0])

    # 写入
    def write(self, path, type):
        data = {'school': 'erxiao', 'studens': ['lili', 'jj']}
        file = open(path, type, encoding='utf-8')
        yaml.dump(data, file)
        file.close()

    def create_yaml(self):
        # 获取当前路径
        current_path = os.path.abspath('.')
        # 创建yaml文件
        yaml_path = os.path.join(current_path, 'create_test.yaml')
        self.write(yaml_path, 'w')


a = YamlTest()

a.read()
# a 追加内容，w 覆盖
# a.write('config.yaml', 'a')


# a.create_yaml()
