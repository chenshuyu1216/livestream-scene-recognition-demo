# 中文直播多模态场景识别演示

[![tests](https://github.com/chenshuyu1216/chenshuyu1216-livestream-scene-recognition-demo/actions/workflows/tests.yml/badge.svg)](https://github.com/chenshuyu1216/chenshuyu1216-livestream-scene-recognition-demo/actions/workflows/tests.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

这是一个面向作品集的脱敏公开版本，用于演示如何将直播划分为 15 秒窗口，融合语音转写与视觉描述，并输出电商、游戏、娱乐才艺、聊天四类场景。

仓库重点展示：

- 多模态窗口数据结构；
- 当前活动分类；
- 三窗口短期平滑；
- 需要连续证据才更新的长期房间类型；
- 可复现的合成数据评估和单元测试。

该仓库为独立重写的教学演示，不包含公司源代码、真实主播数据、生产接口、直播流地址、模型权重或任何凭据。

## 快速运行

```bash
python -m livestream_scene_demo.cli \
  --input data/sample_windows.jsonl \
  --output outputs/demo_predictions.jsonl

python -m unittest discover -s tests -v
python scripts/evaluate_demo.py data/sample_windows.jsonl
```

实习项目中的阶段性结果、适用边界和隐私说明请参阅英文主 README 及 `docs/`。所有数字均明确标注为小样本探索性结果，不代表通用生产准确率。

合成示例运行结果为 12/12，仅用于验证公开演示代码能够按预期工作，不代表真实模型准确率。公开仓库使用可解释规则和合成输入；实习项目中的训练模型、真实数据、采集系统和内部部署信息均未公开。
