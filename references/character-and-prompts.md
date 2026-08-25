# 角色锁定与提示词方法

## 1. 参考图分工

- 身份照片：校正真实脸型、花色、眼睛、耳朵、体型、腿爪、尾巴和配饰。
- 已批准插画：锁定画风、夸张程度、材质、轮廓和头身比。
- 体型锚点：用户明确认为“刚刚好”的单张图，优先级高于形容词。
- 动作参考：只用于姿势，不允许覆盖身份与体型锚点。

优先使用 2–4 张互补参考。参考越多并不必然越稳定；移除冲突、模糊或已被用户否定的图。

## 2. 角色圣经模板

```text
身份：宠物名、物种/品种、年龄感。
脸：脸型、眼睛颜色/形状、鼻口、耳朵、标志花纹。
身体：胸腹厚度、腰线、头身比、腿长、爪大小。
尾巴：数量、长度、粗细、毛量、弯曲方式、连接点。
颜色：背部、腹部、四肢、尾尖的明确色块。
配饰：项圈、吊牌、衣物、准确文字。
画风：写实/半写实/Q版/漫画、线条、材质、夸张程度。
禁止：变胖/过瘦、幼崽化、改变花色、额外部件、错误文字等。
```

不要把“瘦一点/胖一点”不断叠加到提示词。体型漂移时，回到被批准的图像锚点，删除相反的形容词并重新生成一张校准稿。

## 3. 单图提示词结构

按以下顺序组织：

1. 输出类型与用途：单张、方形、微信表情、独立素材；
2. 引用参考图及各自职责；
3. 角色圣经的关键不变量；
4. 本张动作与情绪；
5. 每条肢体/尾巴/道具的位置关系；
6. 文案和符号；
7. 背景、构图、安全边距和禁止项。

### 通用提示词骨架

```text
Create ONE standalone square WeChat sticker of [宠物名].
Use reference A as the absolute identity/body-proportion anchor and reference B
as the approved style anchor. Preserve [身份特征与配饰].

Emotion/action: [明确动作]. Specify the location of each visible forelimb,
hind limb, paw, tail, and prop. Keep the silhouette readable at 240×240.

ANATOMY LOCK: exactly one animal; normal limb count for this species; for a
single-tailed pet, exactly one tail connected once at the lower back; no extra,
duplicated, fused, floating, detached, or cropped parts.

Add only exact text “[文案]” and [必要符号], placed in the reserved area without
covering the face, action, or identifying accessory.
Genuine transparent background; no checkerboard baked in, frame, watermark,
unrelated objects, or random text.
```

提示词不能保证解剖正确，它只是降低风险；必须人工审查。

## 4. 动作设计策略

- 优先选择结构清楚的站、坐、趴、跳、挥手、抱心、捂脸等姿势。
- 使用道具时限制为一个主道具，并写清哪只爪接触它。
- 极端透视、遮挡四肢、尾巴绕身体多圈、双爪与复杂道具交叉，容易产生额外部件。
- 同一套要变化重心、视线、手势和轮廓，不要把 24 张都做成相同坐姿。
- 横幅采用无肢体头肩/胸像；小图标采用脸部近景，减少结构风险和视觉噪声。

### 动态动作提示

动图先把主题拆成起始、预备、展开、接触/发力、峰值、回收和恢复姿势，再为每帧写清重心、视线、四肢、尾巴、嘴和道具关系。不要只写“让猫动起来”；例如“吃瓜”应写出抱住西瓜、靠近、张嘴、咬下、拉开、鼓腮咀嚼、吞咽和再次举起。

质量优先或用户禁止插值时，明确要求每格为完整绘制的真实动作姿势、同一角色身份和一致道具；禁止全图摇晃、裁切缩放、RIFE、光流或形变补帧。完整流程见 [animated-stickers.md](animated-stickers.md)。

## 5. 中文与符号

- 文案以 2–4 个汉字为佳；更长内容要确认在 240×240 仍清楚。
- 仅在用户允许且确有必要时使用“！”“？”“……”、心形、怒气、泪滴、速度线或星光辅助语义；若用户要求无装饰图案，则全部省略。
- 文字生成不稳定时，禁止一遍遍赌模型拼字；生成无字图，再用中文字体确定性排字。
- 后期排字采用粗体、描边、高对比色，并留出边缘安全区；不要遮脸、爪、尾巴或名牌。
- 最终按 manifest 逐字核对，不能只凭缩略图感觉正确。
- 动图只排版一次文字，并在所有帧以相同像素和坐标复用；不得逐帧重新生成文字。

## 6. 返修优先级

1. 身份、花色、体型或尾巴不一致；
2. 多肢、多尾、融合、漂浮、道具穿模；
3. 错字、乱码、文案与动作矛盾；
4. 伪透明、白边、裁切；
5. 构图、颜色和装饰优化。

只返修失败文件，并继续引用同一身份/体型锚点；不要把失败图加入后续参考链。
