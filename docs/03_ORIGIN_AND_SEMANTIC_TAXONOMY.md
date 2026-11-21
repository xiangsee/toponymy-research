# 多轴分类：命名原因 × 词义状态 × 演变事件
版本：0.1（**研究用草案**，允许重叠与未知）

## A. 形成机制（origin_mechanisms，允许多标签）
- NATURAL: 山川、地形、河湖、地貌等自然环境
- SPATIAL: 方位、地理关系、相邻实体定位
- ECOLOGY: 物产、动植物、生态、资源
- SETTLEMENT: 聚落、姓氏、行业、居民活动
- POLITY: 古国、部族、王朝、政治组织和政权
- INFRASTRUCTURE: 渡口、关隘、交通、军政设施
- AUSPICIOUS: 吉祥、理想、价值和文化表达
- COMMEMORATIVE: 纪念人物、事件、政治行动
- INHERITED: 已有地名承继、拆取、组合、移植
- LANGUAGE_CONTACT: 非汉语、方言、音译、意译与混合命名
- UNKNOWN: 暂无法确认

以上不是现行法的分类；INHERITED是形成方式，可能与其他来源机制交叉。

## B. 当代／特定时期的词义状态（semantic_status）
- TOPONYM_DOMINANT: 主要专用于地名；不表示历史上绝无其他含义
- COMMON_COEXISTS: 完整名称有独立且在用的普通词义
- HISTORIC_MEANING: 历史语言语义存在，现今已隐没或少用
- TRANSLITERATED: 现代汉字形式主要体现其他语言音转
- MULTIPLE_GEO: 相同词形指向多个地理实体
- DERIVED_NONGEO: 地名后续衍生非地理指称
- DISPUTED: 词源或语义争议
- UNKNOWN: 无证据判断

这不是单选。特别注意“字义≠词义”，“地名词源≠当前公众理解”。

## C. 历史事件（toponym_events）
NEW_NAME、RENAME、REINSTATE、ALIAS、BORROW、TRANSFER、SPLIT、MERGE、EXPAND、SHRINK、SEAT_MOVE、ADMIN_LEVEL_CHANGE、JURISDICTION_CHANGE、SCRIPT_CHANGE、PRONUNCIATION_CHANGE、LANGUAGE_CHANGE、NAME_DERIVATION、NAME_OBSOLETED。

事件必须有日期区间、对象、史料和不确定性说明。不得把一次政治/建制变化自动解释为名称语义变化。

## D. 对照例子（仅为待核验研究线索）

| 研究对象 | 首先考察的轴 | 待核验事项 |
|---|---|---|
| 邯郸 | TOPONYM_DOMINANT | 商周以前是否可确证更早词源及字义 |
| 朝阳（辽宁） | COMMON_COEXISTS + AUSPICIOUS | 普通词出现与当地正式命名先后 |
| 杭州 | INHERITED | 从余杭取字的文献链，余杭原始词源另证 |
| 敦煌 | DISPUTED | 原始语言、早期记载与后世语义解释 |
| 鄂尔多斯 | LANGUAGE_CONTACT + POLITY | 蒙古语史、部族/地域/市名时序 |
| 上海 | TRANSFER + MULTIPLE_GEO | 上海浦、上海务、镇、县名的先后 |
| 中山 | COMMEMORATIVE | 香山改称中山之正式文件与日期 |

任何行均不可当作最终词源鉴定；先建问题，后求证据。

## E. 本轮新增：地名的「解释史」不等于形成事实（P1-A 2026-11-21）

**命名行为**是当时的人为何采用某名称；**古代释源**是后来的记述者如何解释；**解释流传史**是这一说法如何被其他文献承袭、修正或争论。三者应分别记录。

推荐新增字段：
- `naming_event_evidence`：有无当代命名/更名文书。
- `ancient_etymology_claims`：古籍的释源说法及来源。
- `explanation_provenance`：这些释源说法是否经后世转引，如何变化。
- `modern_linguistic_assessment`：现代词源学、音韵、地望及同时代资料能否支持。
- `limits`：该材料不能证明什么（必须填写）。

**示范**：
- 《汉官仪》经《水经注》《太平御览》保留的六类，是东汉文献系统里对**郡名**的历史概括，不是中国所有地名的排他分类，更不是秦朝制定的政策。
- 《汉书》华阴条同时记录旧名、两次更名和华山地理位置；应在事件史与语义史中分别记录。
- 古代关于酒泉「泉味如酒」及会稽禹会诸侯的解释，是**古人释源材料**，不能未经考证直接当作最初命名事实。

研究札记见 [P1A_01](research/P1A_01_EARLY_TOPONYM_CLASSIFICATION.md)；个案见 [C031华阴](../cases/C031_HUAYIN.md)。
