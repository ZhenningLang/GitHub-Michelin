# computer-vision

> 分类节点。在图片和视频里检测、识别、分析人脸、物体和人——在你自己代码里调用的库和模型。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **DeepFace** | 当你想用一次 Python 调用做人脸比对（是不是同一个人）和一对多人脸检索、模型可切换、阈值现成时用它——但被封装的权重各有许可（Buffalo_L 仅限非商业），TensorFlow 总会被装上，种族／情绪分析在欧盟《人工智能法》下受限。 | B（6/6） | [→](deepface.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [DeepFace](deepface.zh.md) | ✅ | B（6/6） | 一套 API 覆盖 11 个人脸识别模型和约 20 种检测器，阈值现成，带 REST／gRPC 服务和数据库检索——单人维护、0.0.x 版本号、权重许可需逐个继承。 |
| InsightFace／face_recognition／CompreFace／facenet-pytorch | 未收录 | — | DeepFace 页面里点到的人脸识别替代品；本批次（tab-intake）未收录。 |

## 什么该放这里

**计算机视觉的库和模型**：在图片和视频里找到、认出或描述东西——人脸比对与识别、人脸／物体检测、姿态与属性分析——作为你自己代码里的积木。图片转文字在 `ocr`；照片／视频转 3D 在 `3d-reconstruction`；深度估计、CLIP 这类单个研究模型发布放在 `ml-research`。
