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

## F. 出土铭文来源的名称功能与历史地望分离（P1-A v0.3）

商周材料要求额外的**名称功能（referent role）**维度：
- `GEOGRAPHIC_PLACE`：地理地点/地域
- `POLITICAL_CENTER`：政治中心及天下秩序中的空间区域
- `POLITY_OR_GROUP`：政治共同体、族群或方国
- `TITLE_DERIVED_FROM_PLACE`：爵号/封号中使用地名
- `PERSON_OR_LINEAGE`：人名、族名、氏姓（单独标注是否只是同字）
- `ABBREVIATION_OR_GENERIC`：简称、泛称、方位词，不一定是专有地名
- `UNRESOLVED`：字形、句读或指称无法确定

**不能把“字形相同”当成“已证同一实体”**。必须分开记录藏品/原始甲骨来源、铭文中的称谓、具体地望学说及先后次序。

案例：何尊“宅兹中国”见[C032](../cases/C032_HE_ZUN.md)；宜侯夨簋“迁侯于宜”见[C033](../cases/C033_YIHOU_CE_GUI.md)；甲骨「方」字是否专名见[C034](../cases/C034_ORACLE_FANG.md)。

## G. “同字多用”与历史方向严格分开（P1-A v0.4）

“目”在甲骨中可以作普通名词、观察动词、人名或田猎地点，金文又有族氏铭文。**同一汉字具有普通义和专名功能，不等于专名得名于这个普通义。**

“亡终／无终”有商代青铜兵器族氏铭文、春秋无终子政治称谓、汉代右北平郡无终县等材料；李贤唐注则存在“山名→国号→县名”释源，与现代族氏研究的侧重不同。**字形同一、年代先后和不同地理地点的分布并不自动形成名称或族群传承。**

新增关系类型：SAME_GRAPH、SAME_NAME_FORM、MULTIPLE_ROLES_ATTESTED、REFERENT_IDENTIFICATION_HYPOTHESIS、HISTORICAL_DERIVATION_HYPOTHESIS、DERIVATION_SUPPORTED、DISPUTED_LOCATION、UNRESOLVED_DIRECTION。

严格按“古字形→语境句法→专名功能→历史指称→传承因果”五层审查。见 [方法协议](methods/NAME_ROLE_PROVENANCE_PROTOCOL.md)、[C035目](../cases/C035_MU.md)、[C036无终](../cases/C036_WUZHONG.md)。

## H. 双重同一性：文物著录别名 vs 历史名称实体（P1-A v0.5）

**物证著录图（物证 → 不同著录号）**：以甲骨片或经证实的缀合组为对象，链接不同著录书的编号、正反面、藏地、图片、版本。2026-10-31复旦“四方会同”及中央研究院材料来源表是合适的核验入口；仅定位渠道，不意味着已经验证某个编号的全部旧著录。

**历史指称图（文字用例 → 人物、族群、地点等）**：相同字形“目”“无终”出现在不同材料，不能在导入时按字形做同一实体合并；每一条关系都记录“同字／同名／同地／承继推断”何种层级及否证材料。

新增独立于起源、语义、事件分类的关系类型：`CATALOG_ALIAS_CONFIRMED`、`CATALOG_LOOKUP_PENDING`、`SAME_FORM_ONLY`、`COMPETING_HYPOTHESES`、`LATER_COMMENTARY_ATTESTED`、`HISTORICAL_CONTINUITY_UNPROVEN`。

**重要反证**：国家图书馆实物核验甲骨缀合504组中发现39组误缀，说明“已有著录关系”本身亦可修正。这一数字仅对应国图核验样本，不能换算为甲骨著录整体误缀率。

研究札记见 [P1A_05](research/P1A_05_CATALOG_PROVENANCE_AND_ENTITY_IDENTITY.md)。
