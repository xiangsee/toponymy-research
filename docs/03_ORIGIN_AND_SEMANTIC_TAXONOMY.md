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

## I. 行政名称操作独立于原始词源（P1-B v0.6）

新增“名称操作方式”（不按字面制造词源）：
- `ADMIN_ADOPTION_OLD_NAME`：已有地名进入新郡县层级。
- `ADMIN_REASSIGNMENT`：同名县改属不同上级政区（需证明行政归属而不是仅同名）。
- `ADMIN_RECORD_ROUTING`：某名称在邮书、公文、赋税和户籍中承担行政地址功能。
- `IDENTITY_TRANSFER_VIA_MIGRATION`：迁民或仿建旧乡形成新地名（如新丰相关释源）。
- `POLITICAL_RENAME`：政治改制导致的文字更名（如有锡、迁陆）。
- `NAME_PERSISTENCE_WITH_BOUNDARY_UNCERTAINTY`：名称跨时代重见，但县治、郡界是否连续另核。

**反证**：不因“洞庭郡”与“武陵郡”辖若干同名县就默认一个郡完全改名为另一个郡，也不因秦迁陵二十五年为县就断言“迁陵”词语当年首次出现。

见 [P1B札记01](research/P1B_01_QIN_HAN_TOPONYM_STANDARDIZATION.md)。

## J. 自然参照、行政地名与多重指称（P1-B v0.7）

增加两种并行的机制，不混入“词源”单一字段：
- `NATURAL_REFERENCE_TO_ADMIN`：自然河湖或山川名称/方位进入行政区划名（如三川传统释源及汉中）。
- `GEOGRAPHIC_TERM_REUSE`：相同的方位词可在不同地域和时间独立应用（如历史上多个“河南”）。
- `ADMIN_RENAME_WITH_SCOPE_UNCERTAINTY`：秦三川→汉河南有更名文献，但疆界不自动等同。
- `SAME_NAME_DISTINCT_REFERENTS`：两个材料用相同县名却指不同地点，2025年潘国立关于梁县的**待核学术解释**。
- `COUNTY_SEAT_RELOCATION`：县治转移、行政废置后可能使后世旧址误配，卷县/衡雍为**待核学术解释**。
- `GEOGRAPHY_TO_POLITICAL_TITLE`：地域名称进入爵号或王号（汉中→汉王），再到王朝国号；不自动延伸为民族起源的充分条件。

数据里将 **`referent_id`（历史对象）**与 **`name_form`（词形）**分开，并为历史派生关系提供 `proof_level`。所有仅在学术摘要提出的关系必须保留为 `JOURNAL_ABSTRACT_ONLY`。

[指称对象表](../data/p1b_name_referents.csv) / [关系表](../data/p1b_name_referent_relations.csv)。

## K. 生命周期不只有一个时段：存续渠道与行政层级分开（P1-B v0.8）

**跨渠道存续维度**：
- `ADMIN_ACTIVE(level)` / `ADMIN_TERMINATED(level)`：行政层级特定实体；
- `NATURAL_FEATURE_USED`：山川等自然地理名称；
- `CULTURAL_ALIAS_USED`：文学、地方志、民间古称；
- `OLD_NAME_ADOPTED_FOR_NEW_ADMIN`：旧名用于新行政主体；
- `RESTORED_SIMILAR_NAME`：旧行政名恢复，注意行政实体未必相同；
- `STATUS_UNKNOWN`：找不到实际使用或停用证据时不得默认为“已消失”。

**典型反证**：
- 2016邯郸县撤销≠邯郸市撤销；
- 《汉书》赵国“莽曰桓亭”不能降格误解为县级改名；
- 无锡“有锡”短期改名≠锡矿重新出现的实证；
- 姑苏区2012新设≠恢复古代“姑苏区”；
- 1914会稽道≠旧会稽县重新设立；1949新会稽县并不自动与1911前旧县完全同域。

详细规范：[生命周期核验协议](methods/TOPONYM_LIFECYCLE_PROTOCOL.md)；数据：[事件记录](../data/p1b_lifecycle_events.csv)。

## L. 侨置、侨籍与土断：名称迁徙的专门维度（P1-C v0.9）

- `ORIGINAL_REFERENT`：迁出地的原州郡县；
- `QIAO_ADMIN`：迁入地沿用旧名新设的行政机构；
- `LOCAL_TERRITORIAL_ADMIN`：当地早已存在的实土州郡县；
- `MIGRANT_REGISTER`：侨人和原籍户籍身份；
- `TU_DUAN_EVENT`：土断，对户籍/行政政区的实际处理；
- `TERRITORIAL_SUCCESSOR`：侨政区割实或另设的后继行政实体。

名称操作类型：`OLD_NAME_REUSED_IN_MIGRATION`、`QIAO_ADMIN_WITHOUT_SHITU`、`QIAO_TERRITORIALIZATION`、`TU_DUAN_HOUSEHOLD_REGISTRATION`、`QIAO_ADMIN_RENAME`、`QIAO_ADMIN_ABOLISH`。

不得由“南兰陵”的同名直接认定原兰陵消失，也不把土断等同一概撤侨政区。见[P1C札记01](research/P1C_01_QIAO_PREFECTURES_TOPONYM_MIGRATION.md)。
