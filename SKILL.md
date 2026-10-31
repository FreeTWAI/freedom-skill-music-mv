---
name: freedom-skill-music-mv
description: 從一個歌曲構想開始，整理聲音與 MV 敘事、素材來源、製作分工及交付檢查。
---

# 音樂與 MV 製作入門

## 先選一個可以完成的片段

用兩三句話描述歌曲想表達的情緒、對象與場景。第一輪可先做一段 30–60 秒的原創片段或有明確使用範圍的歌曲片段。寫下預計投入時間和希望誰幫忙；不要求先有昂貴設備。

## 把聲音與畫面放在同一張企劃

標記段落，例如前奏、主歌、副歌與結尾；每段記下時間、情緒、歌詞或聲音線索，以及畫面要發生什麼事。先做紙上分鏡或粗剪，確認聲音與影像節奏彼此接得起來。

- 聲音：旋律／歌詞／編曲由誰處理；使用錄音、樂器、樣本或 AI 產出都記錄來源。
- 畫面：真人拍攝、動畫、圖片或混合方式；列出最少需要的鏡頭或素材。
- 分工：每個成果只有一位明確負責人，列出需要誰提供素材、誰回饋。

## 留下可接手的製作紀錄

將音軌、粗剪與最終輸出分版本，保留原始素材的位置 ref。記錄取樣率、影片尺寸、幀率和字幕方式，依這次實際使用的工具決定，不要求所有人使用同一套 DAW 或剪輯軟體。素材取得與使用範圍填入來源表；未知項目清楚標記。

## 用具體問題收回饋

請夥伴先回答「哪一段想表達的情緒最清楚」「哪個轉場讓你分心」「人聲與配樂是否容易聽清楚」。把建議分類為這輪要改、下一輪再做與不採用，留下原因。回饋不是替創作者決定唯一風格。

## 完成時交付

1. 一份歌曲／MV 小企劃與段落分鏡。
2. 一份可播放的片段，或清楚標為未製作的企劃成果。
3. 素材來源表、版本與交付規格。
4. 創作者確認的回饋紀錄與下一步。

只有企劃時標示「企劃完成」，真的有音檔／影片再標示「片段完成」。本手冊不會生成音樂、代你剪輯、代購素材或自動發布。

## AI 輔助生成與 Prompt 企劃 (MV Generation Schemas & Prompts)

若使用 AI 工具輔助音樂或 MV 影像生成，請在企劃中加入以下 Schema 與 Prompt 結構：

### Prompt 結構 (Prompt Template Structure)

將 Prompt 拆分為可預測的區塊，幫助控制生成結果並利於團隊接手：
- **風格與情緒 (Style & Mood)**：定義核心流派、BPM、情緒（例如：`Cyberpunk, synthwave, 120 bpm, energetic, neon lighting, dark background`）。
- **聲音/樂器 (Audio/Instruments)**：指定樂器、人聲特質（例如：`female vocal, clear, heavy bass, electronic synthesizer`）。
- **視覺與畫面 (Visuals)**：鏡頭運動、場景設計、角色動作（例如：`panning shot, a futuristic city with flying cars, highly detailed, 4k`）。

### 生成企劃 Schema (Generation Schema)

在 `RESULT-TEMPLATE.md` 中的段落表，可加入或備註 Prompt 參數：
- `[prompt_audio]`：該段落的聲音生成指令。
- `[prompt_video]`：該段落的畫面生成指令。
- `[seed/reference]`：使用的參考音檔/圖片與 seed 參數，確保風格連貫。

### 素材交接與工作流 (Asset Handover Steps)

在使用 AI 輔助產生大量素材時，確保每一階段的產出物皆可追溯與管理：
1. **標籤與存檔**：將生成的音軌 (stems) 或影像素材依照段落、版本命名（如 `v1_intro_synth.wav`, `v2_chorus_visual.mp4`）。
2. **來源登錄**：即使是 AI 生成素材，也必須在 `SOURCE-REGISTER.md` 中記錄使用的模型、Prompt 摘要與生成日期。
3. **版本控制**：交接給剪輯或混音人員時，提供原始企劃的 Prompt，並標記最終選用的素材 ref。
