# 名称功能与谱系证明协议 v0.1

提出背景：P1-A“目”“无终”显示，字形相同不代表词义相同、专名指称相同、族地传承关系已证。

## 五道审查门槛
1. **GRAPH / 字形**：原甲骨/铜器编号、图片、释文异读。
2. **LEXEME / 词义**：普通词、动词、假借还是专名？完整语境与断句。
3. **ROLE / 功能**：是人名、族名、地名、方国、爵号、山名、县名，还是泛称？
4. **REFERENT / 指称**：具体历史实体与地望；器物出土地、铭文所记地点必须分离。
5. **CONTINUITY / 传承**：是否有独立证据证明同一个对象、迁徙、分封或命名发生？没有证据则“先后未定”。

## 关系标签（并非历史结论）
- SAME_GRAPH：字形相同。
- SAME_NAME_FORM：名称形式相同，但不一定指同一对象。
- MULTIPLE_ROLES_ATTESTED：多种功能已有记载。
- REFERENT_IDENTIFICATION_HYPOTHESIS：两个文本可能指同一地点或人群。
- HISTORICAL_DERIVATION_HYPOTHESIS：名称来源关系是假说。
- DERIVATION_SUPPORTED：名称转化有具体独立证据支撑。
- DISPUTED_LOCATION：地望争议。
- UNRESOLVED_DIRECTION：无法证明从何种名称到何种名称。

## 最小元数据
attestation_id、name_form、time_period、record_type、catalog_identifier、source_ids、source_review_level、usage_context、role_hypothesis、findspot、textual_referent、candidate_geolocation、competing_readings、not_established、verification_next。

## 反证压力测试
- 目：《合集》33367“田目”与《集成》7494“目爵”不自动构成族名派生地名的证据。
- 无终：绥德铜戈、春秋无终子、汉右北平无终县同形；唐注山名说与现代族氏说应并存。
- 宜：江苏丹徒出土簋并不证明铭文“宜”地一定在江苏。
- 方：甲骨文字如果为泛称或简称，不能自动建成独立方国。

**硬原则**：字形相同 ≠ 词同一 ≠ 对象同一 ≠ 已证明名称的转化方向。

本轮修正的 Claim：原“族地同名意味着族名先于地名”的单向假设，应降级为“多角色已见、转化方向待证”。以后每一轮记录 affected_claim / impact_type / verification_next。对于未经授权的原甲骨图片、论文全文，只保留链接与可复核的著录，不上传文件。
