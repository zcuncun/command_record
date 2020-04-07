#!～/usr/bin/python
from absl import flags, app

def main(args):
    del args
    with open(FLAGS.config) as config_f:
        config = json.load(config_f)

if __name__ == "__main__":
    FLAGS = flags.FLAGS
    flags.DEFINE_string('config','default_config.json','配置文件')
    app.run(main)
