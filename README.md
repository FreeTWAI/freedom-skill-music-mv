# 自由工坊 · 音樂與 MV 製作入門手冊

<!-- freedom-repository-guide:start -->
## 在自由工坊的位置

[自由工坊](https://freetwai.com) 讓會員先完成定位、選擇公會並領取 Repo 技能書，再以供貨、商店、開源作品、行銷與小隊共同完成成果。

音樂與 MV 製作公會的原創入門手冊與可填模板。 已有歌曲／MV 企劃、成果模板與素材來源登錄，可手動操作或交給自己的 AI 輔助。

目前是文件技能書，沒有背景服務、會員登入或自動平台同步。

本 repo 的維護者負責「音樂與 MV 製作公會的原創入門手冊與可填模板。」這個模組；公會職稱與自填 GitHub slug 不授予寫入權。

程式／內容入口：[SKILL.md](SKILL.md)、[RESULT-TEMPLATE.md](RESULT-TEMPLATE.md)、[skill-book.json](skill-book.json)、[SOURCE-REGISTER.md](SOURCE-REGISTER.md)。協作先讀 [CONTRIBUTING.md](CONTRIBUTING.md)，讓 Agent 讀 [AGENTS.md](AGENTS.md)；從[本倉 Issues](https://github.com/FreeTWAI/freedom-skill-music-mv/issues)認領、[查看既有 PR](https://github.com/FreeTWAI/freedom-skill-music-mv/pulls)避免重工。

讓音樂創作公會用歌曲與畫面企劃開始第一個成果。 不是自動作曲或產片程式；模型訂閱、聲音肖像及素材授權由實際使用者處理。 會員、公會、技能書授予和公開成果 ref 仍以中央平台 API 的紀錄為準；私人素材留在自己的儲存位置。 跨 repo 的協定由[中央平台](https://github.com/FreeTWAI/freedom-platform)維護。
<!-- freedom-repository-guide:end -->

這是自由工坊原創的入門手冊與可填工作模板。你可以手動完成，也可以請自己使用的 AI 工具協助整理文字與檢查清單。它不是自動作曲、拍攝或產片程式，也沒有安裝或訂閱流程。

1. [在自由工坊註冊與完成定位](https://freetwai.com/)，加入對應公會。
2. Fork 這個 repo，保留來源，按照 [SKILL.md](SKILL.md) 先做一個小成果。
3. 複製 [RESULT-TEMPLATE.md](RESULT-TEMPLATE.md) 記錄企劃、成果與下一步。
4. 素材來源整理在 [SOURCE-REGISTER.md](SOURCE-REGISTER.md)，完成後把可公開的成果連結貼回自由工坊。

公開 fork 放模板和自己願意公開的成果；客戶私密 brief、未公開素材、聯絡方式與憑證請留在你管理的私人位置。這個 repo 不會登入任何平台或代你發布內容。

## 核心模組 (Core Modules)

本專案包含以下核心模組與文件，幫助使用者完成音樂與 MV 的初步企劃與紀錄：

- **`SKILL.md`**：入門教學，提供如何選定片段、整合聲影企劃、留下製作紀錄以及尋求回饋的完整流程。
- **`RESULT-TEMPLATE.md`**：成果卡模板，使用者可複製此文件以記錄每次企劃的細節、負責人、素材參考及製作方式。
- **`SOURCE-REGISTER.md`**：素材來源紀錄表，協助使用者管理所有使用的授權素材、連結與可使用範圍。
- **`skill-book.json`**：技能書設定檔，定義本手冊的基本資訊、版本與入口，提供給自由工坊平台識別。

## 使用範例 (Usage Examples)

你可以透過以下方式來使用本入門手冊：

### 1. 手動執行 (Manual Execution)
- 閱讀 `SKILL.md` 以了解企劃流程。
- 將 `RESULT-TEMPLATE.md` 複製為 `my-song-plan.md`，填入你的歌曲段落與畫面構想。
- 將所有收集到的素材連結填入 `SOURCE-REGISTER.md`，並標明使用限制。

### 2. AI 輔助 Prompt 企劃 (AI-Assisted Prompt Planning)
若你使用 AI 工具生成音樂或影像，可以將 `RESULT-TEMPLATE.md` 提供給 AI，並指示：
- 「請根據以下風格（例如 Cyberpunk、120 BPM），幫我把這段文字擴寫為影片與聲音生成的 Prompt。」
- 在成果模板中加入 `[prompt_audio]` 與 `[prompt_video]` 欄位來保存你的提示詞。
- 生成完成後，將 AI 產出的素材記錄到 `SOURCE-REGISTER.md`。

## API 規格 (API Specifications)

本專案使用 `skill-book.json` 作為設定檔，採用 `freedom.skill-book/v1` 格式：

```json
{
  "format": "freedom.skill-book/v1", // 格式版本標識
  "id": "freedom-skill-music-mv",    // 技能書唯一 ID
  "title": "音樂與 MV 製作入門手冊", // 顯示標題
  "version": "0.1.0",                // 內容版本
  "guild_key": "guild_music_mv",     // 對應的公會識別碼
  "entry": "SKILL.md",               // 技能書主要入口文件
  "execution": "manual_or_member_owned_assistant", // 執行模式
  "repository": "https://github.com/FreeTWAI/freedom-skill-music-mv",
  "license": "NOASSERTION"           // 授權條款
}
```

## 來源與版本

自由工坊新撰寫的入門內容，版本 `0.1.0`；沒有搬用第三方課程或作品。`NOASSERTION` 表示尚未另行宣告授權條款。公會會員身分、主力公會與技能書授予仍以自由工坊平台紀錄為準。
