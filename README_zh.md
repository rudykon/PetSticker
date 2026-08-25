<p align="center">
  <a href="README.md">English</a> · <strong>中文</strong>
</p>

<p align="center">
  <img src="docs/brand-mark.svg" width="430" alt="PetSticker — 微信宠物表情包设计品牌标识">
</p>

<h1 align="center">微信宠物表情包设计</h1>

<p align="center">
  <strong>把自家猫做成会吐槽、会吃瓜、还会满地打滚的微信表情包 🐾</strong><br>
  静态图可以，GIF 也可以——猫负责可爱，这个 Skill 负责把可爱装进聊天框。
</p>

<p align="center">
  <img src="https://img.shields.io/badge/ChatGPT%20%2F%20Codex-Skill-111827?style=flat-square" alt="ChatGPT 和 Codex Skill">
  <img src="https://img.shields.io/badge/Python-%E2%89%A53.9-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.9 或更高版本">
  <img src="https://img.shields.io/badge/%E9%BB%98%E8%AE%A4%E4%B8%93%E8%BE%91-24%20%E5%BC%A0%E8%A1%A8%E6%83%85-2F8F83?style=flat-square" alt="默认 24 张表情">
  <img src="https://img.shields.io/badge/%E6%A8%A1%E5%BC%8F-%E9%9D%99%E6%80%81%20%2B%20GIF-6C63FF?style=flat-square" alt="支持静态和 GIF 动图">
  <img src="https://img.shields.io/badge/%E4%B8%BB%E8%A7%92-%E8%87%AA%E5%AE%B6%E7%8C%AB-E76F51?style=flat-square" alt="主角是自家猫">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-F4A261?style=flat-square" alt="MIT License"></a>
</p>

<p align="center">
  <a href="#概览">概览</a> ·
  <a href="#输入输出示例">输入 → 输出</a> ·
  <a href="#动图效果">动图效果</a> ·
  <a href="#工作流">工作流</a> ·
  <a href="#交付内容">交付内容</a> ·
  <a href="#快速开始">快速开始</a> ·
  <a href="#自动校验">自动校验</a> ·
  <a href="#仓库地图">仓库地图</a> ·
  <a href="#许可证">许可证</a>
</p>


> [!NOTE]
> 这里没有“猫咪表情包合规审计委员会”。脚本负责数尺寸、帧数和文件大小；你只要负责确认两件事：**这还是我家猫吗？够不够好笑？**

<a id="概览"></a>
## 🐾 概览

PetSticker 就干一件事：把你家猫那些经典表情、欠欠的眼神和莫名其妙的小动作，变成一套真正能拿来聊天的表情包。它支持静态 PNG 和 GIF 动图，也会顺手帮你盯住那些很破坏气氛的问题——比如猫突然换脸、长出第五条腿、文字开始蹦迪，或者所谓的“透明背景”其实是一块白板。

| 想要什么 | Skill 怎么帮忙 | 最后得到 |
| --- | --- | --- |
| 还是那只猫 | 记住脸型、花色、体型、尾巴、项圈和名牌 | 换了 24 个梗，也不会像换了 24 只猫 |
| 别突然变异 | 检查腿、爪、尾巴、道具接触和动作关系 | 不多脚、不双尾，西瓜也不会穿过猫爪 |
| 字别写错，也别乱跑 | 文案尽量短；不稳定时单独排字并锁死位置 | 小尺寸能看懂，动图里文字不蹦迪 |
| 背景真的透明 | 检查 Alpha 和边缘残色 | 没有白底、绿边和假棋盘格 |
| 动起来，但别整张摇 | 直接生成连续动作帧，再检查节奏和完整循环 | 猫在表演，画布站稳，过渡不抽风 |
| 文件别散落一地 | 自动检查数量、尺寸、格式、命名和目录 | 一套收得整整齐齐的成品 |

<a id="输入输出示例"></a>
## 🖼️ 输入 → 输出示例：布鲁 · 职场办公

这里拿布鲁做个示范：从一张猫猫照片出发，保住它的大直立耳、暖灰棕短毛、轻巧体型和丰富小表情，再把它送去体验一整套打工猫日常。

### 📸 输入：宠物参考图

<p align="center">
  <img src="docs/showcase/workplace/input-reference.jpg" width="280" alt="经过裁切的布鲁猫输入参考照片">
</p>

<p align="center"><sub>主角登场：布鲁，一只还不知道自己马上要上班的猫。</sub></p>

<p align="center"><strong>↓ 认识这只猫 → 想好梗 → 分批出图 → 大家一起找茬 ↓</strong></p>

### 💬 输出：表情成品选图

| 日常办公 | 求助、压力与阶段节点 |
| --- | --- |
| ![打卡、电脑崩了、摸鱼中和搞定表情](docs/showcase/workplace/output-workday.png) | ![求指导、头秃了、周五快乐和升职加薪表情](docs/showcase/workplace/output-milestones.png) |

<p align="center"><sub>从 24 张成品里挑了 8 张露脸，其余猫猫还在认真摸鱼。</sub></p>

### 🏙️ 配套素材：详情页横幅

<p align="center">
  <img src="docs/showcase/workplace/detail-banner.jpg" width="750" alt="布鲁猫坐在明亮办公室的电脑桌前">
</p>

没错，认真上班的是猫，真正摸鱼的是我们。

<a id="动图效果"></a>
## 🎬 动图效果：布鲁 · 网络热梗

猫负责表演，文字负责原地站好。下面 4 张都是这个 Skill 实际做出来的 GIF：240×240、12 张直接生成的连续动作帧、完整循环 2.00 秒、透明背景、单张低于 500 KB。没有 RIFE，没有光流插帧，也没有偷懒让整张图左右乱晃。

<table>
  <tr>
    <td align="center"><strong>吃瓜｜道具接触与咀嚼</strong><br><img src="docs/showcase/animated/02-eating-watermelon.gif" width="210" alt="布鲁猫抱住西瓜并咬下咀嚼的动态表情"></td>
    <td align="center"><strong>绷不住了｜全身翻滚大笑</strong><br><img src="docs/showcase/animated/04-laughing.gif" width="210" alt="布鲁猫从忍笑到翻滚大笑的动态表情"></td>
  </tr>
  <tr>
    <td align="center"><strong>快跑｜连续奔跑姿态</strong><br><img src="docs/showcase/animated/08-running.gif" width="210" alt="布鲁猫连续蹬地奔跑的动态表情"></td>
    <td align="center"><strong>感谢｜完整鞠躬循环</strong><br><img src="docs/showcase/animated/22-thanks.gif" width="210" alt="布鲁猫合爪鞠躬感谢的动态表情"></td>
  </tr>
</table>

想看看猫到底怎么动起来的？[`references/animated-stickers.md`](references/animated-stickers.md) 里写了语义拆帧、连续动作图、文字锁定、透明背景修复、GIF 节奏检查和返修方法。

<a id="工作流"></a>
## 🧩 怎么把猫送进聊天框

```text
[一张猫猫好照片]
      |
      v
[猫设小档案] -> [24 个梗和动作] -> [一小批一小批地画]
                                        |
                                        v
                                   [找茬时间]
                                   |       |
                                 有问题    好耶
                                   |       |
                                   v       v
                               [只修这张] [打包下班]
                                   |
                                   +------> 再看一眼
```

找茬主要分三轮：

| 这一轮 | 看什么 | 看到什么就返工 |
| --- | --- | --- |
| **1. 还是不是它** | 脸型、花色、眼睛、耳朵、胖瘦、腿爪、尾巴和配饰 | 突然换猫、忽胖忽瘦、花纹和名牌偷偷变了 |
| **2. 猫有没有穿模** | 腿和尾巴数量、裁切、道具接触、姿势、文案和每张图的区别 | 多肢、双尾、部件融合、不可能动作、错字或看不懂 |
| **3. 文件乖不乖** | 数量、像素、格式、透明度、大小、命名、目录和清单 | 少文件、尺寸错、假透明、JSON 或命名出问题 |

哪张有问题就只修哪张，不用把全家猫都推倒重来。脚本会数数和查文件，但“像不像”和“好不好笑”还是人说了算。

<a id="交付内容"></a>
## 📦 猫猫全家桶里有什么

默认一套完整静态专辑会拿到：

| 素材 | 默认数量 | 说明 |
| --- | ---: | --- |
| 独立表情 PNG | 24 | 覆盖不同情绪、姿势和聊天语境 |
| 表情形象头像 | 1 | 透明 240 × 240 PNG |
| 详情页横幅 | 1 | 不透明 750 × 400；优先头肩或胸像构图 |
| 表情封面图 | 1 | 透明 240 × 240 PNG |
| 聊天页图标 | 1 | 透明 50 × 50 PNG |
| 赞赏引导图 | 可选 1 | 750 × 560 |
| 赞赏致谢图 | 可选 1 | 750 × 750 |
| 素材清单、猫设小档案、检查报告 | 3 | 以后找图和返修时不用翻到怀疑猫生 |

默认发布目录：

```text
project/
├── references_private/        # 参考照片：猫猫本猫
├── work/                      # 草稿、工作图和返修现场
└── release/
    ├── stickers/              # 01_*.png … 24_*.png，排队出道
    ├── assets/
    │   ├── character_avatar.png
    │   ├── detail_banner.jpg
    │   ├── album_cover.png
    │   ├── chat_icon.png
    │   ├── tipping_prompt.jpg # 可选
    │   └── tipping_thanks.jpg # 可选
    ├── manifest.json
    ├── character_bible.md
    └── qa_report.md
```

<a id="快速开始"></a>
## 🚀 三步开撸

### 1. 📥 克隆 Skill

```bash
git clone https://github.com/rudykon/PetSticker.git
cd PetSticker
```

在支持 Skills 的 ChatGPT/Codex 环境中，把整个仓库当成一个 Skill 安装或加载。`SKILL.md`、`agents/`、`assets/`、`references/` 和 `scripts/` 要待在一起，别把猫的工具箱拆散了。

### 2. 🧰 安装校验脚本依赖

```bash
python3 -m pip install Pillow
```

### 3. 🐱 调用 Skill

```text
$wechat-pet-sticker-designer
```

示例请求：

```text
使用 $wechat-pet-sticker-designer，根据我上传的宠物参考图制作一套可提交
微信平台的静态表情包。保持已确认的体型和名牌，使用真实透明背景，并逐图
检查多肢、多尾、中文错字和风格漂移。
```

除非真的少了一个会改变结果的关键选择，否则 Skill 会直接认识你的猫、规划整套表情，再从一小批开始出图——先看对不对味，再让猫全面出道。

<a id="自动校验"></a>
## 🔍 让脚本数数，别让它评猫

尺寸、数量、帧数和文件名看久了容易眼花，这些交给脚本：

```bash
python3 scripts/validate_album.py /absolute/path/to/project/release \
  --expected-stickers 24 \
  --with-tipping \
  --require-qa-docs
```

再把 24 张排成一页，哪张猫设飞了，一眼就能抓住：

```bash
python3 scripts/make_contact_sheet.py \
  /absolute/path/to/project/release/stickers \
  /absolute/path/to/qa_overview.png
```

需要机器可读报告时添加 `--json`。GIF 还可以顺便检查帧数、速度、完整循环和逐帧透明：

```bash
python3 scripts/validate_album.py /absolute/path/to/project/release \
  --expected-stickers 24 --allow-gif-stickers \
  --gif-frames 12 --gif-loop-ms 2000 \
  --require-infinite-loop --require-transparent-gif \
  --require-clear-gif-edges --require-qa-docs

python3 scripts/make_animation_sheet.py \
  /absolute/path/to/project/release/stickers \
  /absolute/path/to/all_frames.png --expected-frames 12
```

<a id="仓库地图"></a>
## 🗺️ 想往里翻？地图在这

| 路径 | 用途 |
| --- | --- |
| [`SKILL.md`](SKILL.md) | 猫猫变表情包的主流程和关键规则 |
| [`agents/openai.yaml`](agents/openai.yaml) | Skill 显示名称、默认提示词、产品策略和图标映射 |
| [`references/wechat-assets.md`](references/wechat-assets.md) | 微信素材尺寸、格式、透明度和大小要求 |
| [`references/character-and-prompts.md`](references/character-and-prompts.md) | 角色圣经、提示词、中文排字和返修策略 |
| [`references/animated-stickers.md`](references/animated-stickers.md) | 动图语义拆帧、直接生成、透明处理、检查和优化方法 |
| [`references/qa-and-delivery.md`](references/qa-and-delivery.md) | 最后一轮找茬、返修和整理方法 |
| [`assets/`](assets) | 角色圣经、清单、QA 报告模板和 Skill 图标 |
| [`scripts/validate_album.py`](scripts/validate_album.py) | 专辑结构与图片文件的确定性校验 |
| [`scripts/make_contact_sheet.py`](scripts/make_contact_sheet.py) | 生成带编号的视觉总览图 |
| [`scripts/make_animation_sheet.py`](scripts/make_animation_sheet.py) | 生成逐张逐帧的动态 QA 总览图 |

<a id="许可证"></a>
## 📜 许可证

仓库里的原创说明、模板和脚本采用 [MIT License](LICENSE)。宠物照片、表情成品、字体和第三方素材按各自的规则使用。简单说：**代码欢迎一起玩，猫还是各家的猫。**
