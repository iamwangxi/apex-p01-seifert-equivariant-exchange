# 交换复形的固定点可缩性及不可压缩 Seifert 曲面应用

**定理 E：有限群保复杂度地作用于任意交换复形时，几何实现的不动点空间非空且可缩。** 使用弱拓扑，不要求局部有限、可数、有限维或复杂度纤维有限，也不要求复杂度单射。**推论 E′：对于实际光滑作用于非平凡纽结对的有限群，在目标论文 Theorem A 所用的同一外部分析输入 (U)、(E)、(Fin) 成立的条件下，得到不可压缩 Seifert 曲面复形的同样结论。**

## 目标版本与结果

本仓库配套一份拟申请 **breakthrough contribution（valuable generalization）** 的投稿。目标是 Apex Intelligence 署名的 *Contractibility of the complex of incompressible Seifert surfaces: the knot case of Kakimizu's problem*，**2026 年 9 月 11 日比赛版，48 个印刷页**。目标 PDF 的 SHA-256：

`34f17d7d99780d3fd3626d9e5d7b35d6aa76661c404f191b6df341b300c0c06f`

比赛版引言印刷 p. 2 把等变推广列为未处理事项。作者后续 arXiv:2609.09224v2（2026 年 9 月 12 日）§8.4、印刷 pp. 67–68 也未给出不动点空间可缩性证明。v2 已有“不变 apex 单形的重心固定”的观察；本仓库不将其算作新贡献。

证明不打破复杂度平级。关键补充引理是：同一非最低复杂度的非空有限面，其严格较低共同链接非空、直径至多为 2，并继承交换结构。随后用不变面链精确建模不动点空间，计算上纤维，按复杂度序型作普遍超限归纳。不可数极限阶段也使用弱 CW 拓扑。

## 范围与限制

交换复形是非空、连通的 flag 复形，配有良序复杂度；每个距离为 2 的点对，其共同邻点集合有一个与全体共同邻点相等或相邻的 apex，并存在复杂度严格低于较大端点值的这样的 apex。不要求全局选取或等变选取 apex。

定理只处理有限保复杂度群作用，没有推广 Przytycki–Schultens 对最小亏格复形的任意子群结论。Hensel–Osajda–Przytycki 的无限图判据要求逐点有限 dismantling projections、投影族等变、没有无限 clique；使用不变 clique 的分支还要求 synchronised。交换公理本身没有给出这些数据。本仓库不证明这类投影不存在，也不声称已经排除全部既有判据的覆盖可能。

穷尽计算显示，**至多 9 个顶点的有限交换图全部可拆**，因此这个规模内的固定点结论已被 HOP 的有限图定理覆盖。一般有限交换图是否都可拆仍未证明；有限情形不作为独立新颖性主张。对于满足 PS 数据条件的有限群，其不变单形从 $`MS`$ 嵌入 $`IS`$ 即给已有非空性（已核预印本 p. 5）；本应用的候选增量是整个 $`IS`$ 不动点空间的可缩性。

Seifert 应用在目标论文式 (2) 的精确 warped collar 范围内构造不变几何数据，但不独立重证外部面积极小化输入，也不认证目标论文全部内部分析论证。几何固定点只给有限不变单形，即可同时取不交代表的有限组曲面同痕类；不推出单个不变嵌入曲面或整族等变实现。只有有限映射类子群而没有实际群作用时，还需另行实现。

## 仓库导览

- [proof/theorem-e.md](proof/theorem-e.md)：定理、约定、保平级的次水平测地线、最低层、严格较低共同链接，对应 §§1–3。
- [proof/fixed-point-model.md](proof/fixed-point-model.md)：不变面模型、直接证明的上纤维引理、有限包含零伦准则，对应 §§4–5。
- [proof/induction.md](proof/induction.md)：普遍超限归纳的基础、后继、极限与依赖清单，对应 §6。
- [proof/seifert-application.md](proof/seifert-application.md)：不变几何数据与条件式推论 E′，对应 §7。
- [proof/literature.md](proof/literature.md)：比赛版、v2、PS 与 HOP 的已核对照、计算证据和新颖性边界。
- [scripts/README.md](scripts/README.md)：复现命令、依赖版本、实测运行时间和结果含义；同目录提供两个 Python 脚本和结果 JSON。
- [sources/bibliography.md](sources/bibliography.md)：实际核对的版本、定理、印刷页码、公开获取方式与核验限制。
- [README.md](README.md)：对应英文说明。
- [LICENSE](LICENSE)：原始散文 CC BY 4.0，代码 MIT。
- [MANIFEST.sha256](MANIFEST.sha256)：除清单自身外的所有仓库文件哈希。

两组计算已完整重跑，全部非时间字段与提供的原始记录一致：474 个 atlas 交换图，60,000 次随机尝试中的 25,686 个交换图，34,007 次固定空间同调检查，以及全部 818,295 个九顶点扩展候选。计算独立于定理 E 的证明；零约化同调没有被当作可缩性证明。

在仓库根目录运行 `shasum -a 256 -c MANIFEST.sha256`（macOS）或 `sha256sum -c MANIFEST.sha256`（GNU coreutils）可核对公开包字节。重跑计算会覆盖 JSON 并改变哈希；清单核对不等于数学认证。

## 复核状态与 AI 声明

全新上下文 GPT-6.1 Sol 对抗复核未发现抽象证明或不变几何数据构造的数学断点。报告的两项文献修补与两项澄清建议已纳入：HOP 覆盖关系仍未决，投影条件完整列明，分析输入按完整陈述使用，并明确 PS 数据条件下的非空性已有来源。

GPT-6.1 Sol, in OpenAI Codex under human direction, developed the proof, ran the computations where applicable, and drafted this text; a separate GPT-6.1 Sol session in a fresh context performed an adversarial review. Claude planned the work, checked key steps against the sources, and reviewed and edited the final text. No human expert has certified the work.

## 版本说明

本版本与 `f8828558f0ed9a47d269713db93fc63d138dadb9` 相比，只改了公式的写法。GitHub 的 Markdown 处理会去掉 `$...$` 里的 `\{`、`\,` 等反斜杠转义，还有部分公式没被识别，所以全部公式改用 GitHub 的原样数学语法。数学文字没有任何改动。

## 许可

原创散文在适用权利存在的范围内采用 **CC BY 4.0**。署名 **apex-p01-seifert-equivariant-exchange contributors**，链接许可、标明修改，并在可用时注明仓库地址与版本。`scripts/` 中的代码采用 **MIT License**。外部论文和 NetworkX 保留各自权利，详见 [LICENSE](LICENSE)。
