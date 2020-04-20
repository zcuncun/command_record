#! /usr/bin/python
# -*- coding: utf-8 -*-

from absl import flags, app, logging


def main(args):
    del args
    with open(FLAGS.config) as config_f:
        config = json.load(config_f)

if __name__ == "__main__":
    logging.set_verbosity(logging.DEBUG)
    # logging.set_verbosity(logging.INFO)
    FLAGS = flags.FLAGS
    flags.DEFINE_string('config','default_config.json','配置文件')
    app.run(main)
