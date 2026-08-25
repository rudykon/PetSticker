---
name: wechat-pet-sticker-designer
description: Design, generate, animate, repair, review, resize, optimize, package, or prepare a personalized static or GIF pet sticker album for the WeChat Sticker Open Platform. Use when an AI agent must turn pet photos or an approved character reference into individual sticker files and companion assets, plan captions/scenes or semantic animation frames, preserve pet identity and body proportions, keep animated text static, enforce real transparency, prevent extra limbs/tails, check Chinese text and GIF timing, meet size limits, create submission-ready folders or ZIPs, or diagnose a rejected/defective pet sticker asset.
---

# 微信宠物表情包设计

以宠物参考图为身份锚点，完成“设计—生成—审查—规格化—打包”闭环。视觉质量与平台合规同等重要；未经逐图审查的批量生成不能作为成品交付。

本流程不绑定某个模型、编辑器或 AI 助手。只要当前环境能读取本仓库的 Markdown 说明、使用图像生成/编辑能力并运行所需脚本，就可以执行；是否支持 `$skill-name` 形式的原生调用不影响工作流本身。

## 先读取所需资源

- 开始任何制作或验收前，读取 [wechat-assets.md](references/wechat-assets.md)。
- 需要建立角色、写生成提示词、控制中文或返修时，再读取 [character-and-prompts.md](references/character-and-prompts.md)。
- 制作、检查或优化 GIF 动图时，读取 [animated-stickers.md](references/animated-stickers.md)。
- 需要人工终检、交付或处理异常素材时，再读取 [qa-and-delivery.md](references/qa-and-delivery.md)。

若用户给出更新的官方文档，以该文档为准；记录与本 Skill 默认表格的差异，不要用旧规格覆盖新要求。

## 工作流

### 1. 确认任务边界

从用户材料中提取：

- 宠物名字、物种/品种、花色、眼睛、耳朵、口鼻、体型、尾巴、配饰和不可改变特征；
- 画风、主题、表情数量、静态或动态、是否启用赞赏；
- 每张图的文案/语义、输出目录、命名语言和是否需要 ZIP；
- 用户提供的官方规范或自定义尺寸。

仅在缺少会改变结果的关键选择时提一个简短问题。若用户已给出宠物照片和明确主题，可直接制定清单并开始。

### 2. 建立角色圣经与体型锚点

选择 2–4 张清晰参考图覆盖正脸、侧身、全身、尾巴和配饰；若已有用户批准的插画，将其设为首要风格与比例锚点，真实照片负责校正身份细节。

在生成前写出一份简短角色圣经，至少锁定：

- 头脸结构与标志性花纹；
- 健康体型、胸腹厚度、头身比、腿和爪的粗细；
- 尾巴数量、长度、粗细、形状与连接点；
- 项圈、名牌等配饰及准确文字；
- 禁止项，例如“不要变胖、不要拉成长条、不要幼崽化”。

不要只靠文字重新猜角色。每次生成都引用同一组已确认锚点；一旦用户指定某张图“比例刚好”，将其升级为唯一体型标尺。

### 3. 先规划，再生成

先列出完整素材清单。默认一套完整专辑为：

- 24 张独立静态表情；
- 1 张表情形象头像；
- 1 张详情页横幅；
- 1 张表情封面图；
- 1 张聊天页图标；
- 启用赞赏时，1 张赞赏引导图和 1 张赞赏致谢图。

若用户要动态专辑，先在 manifest 中记录画布、帧数、逐帧延时、完整循环时长、循环方式、透明背景、文字是否静止、体积上限和插值许可。不要默认套用某个帧数或速度；按用户要求设计，并使用 [animated-stickers.md](references/animated-stickers.md) 的语义拆帧方法。

让 24 个表情覆盖不同姿势、面部表情和使用语境；避免仅替换文案。优先使用 2–4 个汉字或通用符号提升小尺寸理解度，但不是每张都强行加字。

把生成拆成 3–4 张的小批次。首批通过身份、体型、文字和解剖审查后再扩批；发现系统性偏胖、偏瘦或风格漂移时，暂停后续生成并重设锚点。

### 4. 生成独立原图

使用可用的图像生成/编辑能力，每次为一个最终资产调用一次生成；可并行生成互不依赖的小批次。先查看所有要引用的图像；编辑现有图时带上对应参考图，创建新图时也要在提示词中明确各参考图的职责。把角色圣经、动作、文字、背景和解剖约束写进每个提示词。

对完整身体画面明确要求：一只宠物、该物种正常的四肢数量、单尾动物仅一条尾巴、无重复/融合/漂浮/裁断部件。复杂道具动作要说明每只爪的位置及道具与身体的边界。

动图不得用整张贴纸的平移、旋转、缩放、抖动或裁切冒充角色动作。需要质量优先或用户禁止插值时，每帧直接生成完整动作图；失败过渡帧应重新生成，不得用 RIFE、光流或形变补帧替代真实中间姿势。

对详情页横幅优先采用头肩或胸像构图，不展示四肢和尾巴；横幅完全不放文字。该构图能从源头降低多脚、多尾和文字违规风险。

### 5. 处理文字与透明背景

中文准确性高于装饰效果。若生成模型不能稳定输出准确中文：

1. 生成无文字画面并预留文案区；
2. 使用支持中文的字体在后期确定性排字；
3. 对照清单逐字复核，不接受形近错字、乱码或随机英文。

动图文字只生成和排版一次，再以同一坐标合成到全部帧；手写字形的倾斜、大小和基线差异也必须固定。不得让模型在每帧重新生成文字。

透明素材必须含真实 Alpha。棋盘格图案、白底或黑底都不等于透明；在彩色底上检查白边、灰边、绿边、残留棋盘格和方形底板。不要用会误删宠物浅色毛发的粗暴颜色抠图；必要时重新生成或使用精细蒙版。

### 6. 每批执行三层门禁

不得只检查文件尺寸。

1. **身份与体型门**：与锚点比较脸型、花色、眼睛、耳朵、胸腹厚度、头身比、腿爪、尾巴和配饰。
2. **结构与语义门**：在原始分辨率检查部件数量/连接关系；在目标小尺寸检查动作、文字、符号和 24 张之间的区分度。
3. **文件规格门**：检查数量、尺寸、格式、Alpha/不透明要求、压缩阈值、命名和目录。

动图再增加 **时间轴与过渡门**：检查帧数、逐帧延时、总循环时长、首尾衔接、静态文字锁定、相邻帧身份/解剖/道具连续性，以及实际播放速度。

任何一层失败都只返修失败文件，然后重新走三层门禁。多肢、多尾、文字错误、体型漂移或伪透明属于阻断性缺陷，不能带病打包。

### 7. 规格化并自动检查

保留高分辨率工作源；从工作源导出平台尺寸，不要反复缩放成品。

采用以下目录结构，或在运行脚本时用参数映射用户的结构。可复制
`assets/` 中的三个模板作为起点：

```text
project/
├── references_private/        # 原始宠物照片；默认不进入分享包
├── work/                      # 高分辨率源、草稿、返修稿
└── release/
    ├── stickers/              # 01_*.png … 24_*.png
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

运行：

```bash
python3 scripts/validate_album.py /absolute/path/to/project/release \
  --expected-stickers 24 --with-tipping --require-qa-docs
python3 scripts/make_contact_sheet.py \
  /absolute/path/to/project/release/stickers /absolute/path/to/qa_overview.png
```

动态专辑还应运行 `validate_album.py` 的 GIF 参数并生成逐帧总览；完整命令见 [animated-stickers.md](references/animated-stickers.md)。

自动检查通过不代表视觉审查通过；必须查看总览图，并按 [qa-and-delivery.md](references/qa-and-delivery.md) 逐张人工确认。

### 8. 交付

最终目录只放正式素材、清单和必要说明，不混入草稿。每个表情必须是独立文件。默认不把用户的私人宠物照片放进分享包；仅在用户明确要求可审计参考包时加入获准的参考图。仅在用户要求时创建 ZIP；压缩后执行完整性测试并核对文件数量。

向用户报告：文件构成、自动检查结果、人工审查范围、返修项（若有），以及成品/预览的可点击路径。不得把“脚本通过”表述成已经自动证明不存在多肢、多尾或体型漂移。

## 强制停止条件

- 参考图不足以判断宠物身份或体型，且不同选择会显著改变结果；
- 官方规范与用户要求冲突，无法同时满足；
- 中文文案、宠物名牌或素材数量仍不确定；
- 关键文件存在多肢、多尾、裁切、伪透明或错字，尚未返修；
- 生成工具无法产出独立文件，却准备把拼图当作最终表情交付。
- 用户禁止插值或要求直接生成动作帧，却仍准备使用 RIFE、光流、形变补帧或整图摇晃。

遇到这些情况时，先修复或向用户确认，不要继续批量扩展或宣称完成。
