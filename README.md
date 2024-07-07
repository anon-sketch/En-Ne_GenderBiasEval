# Gender Bias in Nepali-English Machine Translation
## A Comparison of LLMs and Existing MT Systems


### MT Systems

- 5 MT systems were initially considered: 2 existing MT systems (Google Translate, IndicTrans2 [(Gala et.al.)](https://arxiv.org/abs/2305.16307)) and 3 LLMs(GPT3.5, GPT4o and BLOOM-7b). 
- Evaluated on BLEU benchmark to identify if they are capable of accurate translation

|MT Systems| FLORES200 | IN22-Gen | IN22-Conv |
| ----------- | ----------- | ----------- | ----------- |
| **Google Translate** | **46.5\*** | **46.8\*** | **43.1\*** |
| **IndicTrans2** | **46.3** | **45.1** | **42.1** |
| **GPT-3.5** | 26.1 | 27.1 | 28.4 | 
| **GPT-4o** | **41.6** | **43.7** | **41.0** |
| **BLOOM7B** | 15.5 | 15.4 | 21.2 | 


- Considered Google Translate, IndicTrans2 and GPT-4o for the upcoming experiments.


### Benchmark Creation

1. **Gender Neutral Approach**
- Dataset: Equity Evaluation Corpus-Nepali (EEC-Nepali)

2. **Simple Gender-Specific Context**
- Dataset: OTSC-Nepali

3. **Complex Gender-Specific Context**
- Dataset: WinoMT-Nepali

<hr>

For the details in benchmark creation and the final results, refer to the paper <a href="https://drive.google.com/file/d/1rA-P8u8YwXJdF0liczH6gHkc7isRLARc/view?usp=sharing" target="_blank">here</a>.
