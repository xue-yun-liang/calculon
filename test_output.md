### Testing top level --help
### Testing "llm-all-executions" --help
### Testing "lae" --help
### Testing "llm" --help
### Testing "llm-validation" --help
### Testing "lv" --help
### Testing "llm-optimal-execution" --help
### Testing "loe" --help
### Testing "version"
0.1.0
### Testing "v"
0.1.0
### Testing "llm-parameter-calculator" --help
### Testing "lpc" --help



### Testing llm-parameter-calculator
anthropic-52B   -> 52.033 G
chinchilla      -> 64.869 G
gopher-280B     -> 258.587 G
gpt3-13B        -> 12.941 G
gpt3-175B       -> 174.616 G
lamda           -> 103.526 G
megatron-126M   -> 125.949 M
megatron-1T     -> 1.008 T
megatron-22B    -> 22.074 G
megatron-40B    -> 39.096 G
megatron-5B     -> 5.051 G
palm-540B       -> 428.625 G
turing-530B     -> 529.601 G



### Testing llm
models/anthropic-52B.json
models/chinchilla.json
models/gopher-280B.json
models/gpt3-13B.json
models/gpt3-175B.json
models/lamda.json
models/megatron-126M.json
models/megatron-1T.json
models/megatron-22B.json
models/megatron-40B.json
models/megatron-5B.json
models/palm-540B.json
models/turing-530B.json



### Testing llm-validation


Now running test: seqsel_fig1
Analyzing megatron-22B none
Analyzing megatron-22B seqsel
Analyzing gpt3-175B none
Analyzing gpt3-175B seqsel
Analyzing turing-530B none
Analyzing turing-530B seqsel
Analyzing megatron-1T none
Analyzing megatron-1T seqsel
*Params & Opt,|,none,,,|,seqsel,,,
Model,|,Profile,Calc,Delta,|,Profile,Calc,Delta,
megatron-22B,|,45.5625,40.62,10.84%,|,45.5625,40.62,10.84%,
gpt3-175B,|,45.5625,40.93,10.17%,|,45.5625,40.93,10.17%,
turing-530B,|,31.640625,29.30,7.40%,|,31.640625,29.30,7.40%,
megatron-1T,|,32.958984375,31.13,5.55%,|,32.958984375,31.13,5.55%,
Ave,,8.49%
Max,,10.84%
,
*Activations,|,none,,,|,seqsel,,,
Model,|,Profile,Calc,Delta,|,Profile,Calc,Delta,
megatron-22B,|,59.25,59.44,-0.32%,|,9.5625,10.40,-8.74%,
gpt3-175B,|,66.84375,66.94,-0.14%,|,12.3515625,12.69,-2.75%,
turing-530B,|,114.0234375,114.18,-0.14%,|,23.076171875,23.56,-2.12%,
megatron-1T,|,131.25,131.45,-0.15%,|,26.5625,27.17,-2.30%,
Ave,,2.08%
Max,,8.74%
,


Now running test: seqsel_fig7
Analyzing megatron-22B none
Analyzing megatron-22B seq
Analyzing megatron-22B sel
Analyzing megatron-22B seqsel
Analyzing megatron-22B full
Analyzing gpt3-175B none
Analyzing gpt3-175B seq
Analyzing gpt3-175B sel
Analyzing gpt3-175B seqsel
Analyzing gpt3-175B full
Analyzing turing-530B none
Analyzing turing-530B seq
Analyzing turing-530B sel
Analyzing turing-530B seqsel
Analyzing turing-530B full
Analyzing megatron-1T none
Analyzing megatron-1T seq
Analyzing megatron-1T sel
Analyzing megatron-1T seqsel
Analyzing megatron-1T full
Activations,|,none,,,|,seq,,,|,sel,,,|,seqsel,,,|,full,,,
Model,|,Profile,Calc,Delta,|,Profile,Calc,Delta,|,Profile,Calc,Delta,|,Profile,Calc,Delta,|,Profile,Calc,Delta,
megatron-22B,|,100.0%,100.00%,0.00%,|,66.84%,66.92%,-0.11%,|,49.42%,43.17%,12.66%,|,16.18%,17.49%,-8.13%,|,7.64%,9.96%,-30.41%,
gpt3-175B,|,100.0%,100.00%,0.00%,|,62.04%,62.03%,0.02%,|,56.53%,48.32%,14.52%,|,18.49%,18.96%,-2.54%,|,8.71%,9.63%,-10.55%,
turing-530B,|,100.0%,100.00%,0.00%,|,58.31%,58.41%,-0.17%,|,62.04%,52.79%,14.91%,|,20.27%,20.64%,-1.82%,|,9.42%,10.37%,-10.04%,
megatron-1T,|,100.0%,100.00%,0.00%,|,58.31%,58.41%,-0.18%,|,62.04%,52.82%,14.86%,|,20.27%,20.67%,-1.99%,|,9.42%,10.44%,-10.81%,
Ave,,6.69%
Max,,30.41%
,


Now running test: seqsel_tab5
Analyzing megatron-22B full
Analyzing megatron-22B seqsel
Analyzing gpt3-175B full
Analyzing gpt3-175B seqsel
Analyzing turing-530B full
Analyzing turing-530B seqsel
Analyzing megatron-1T full
Analyzing megatron-1T seqsel
End-to-end,|,full,,,,|,seqsel,,,,
Model,|,Profile,Calc,Delta,GiB,|,Profile,Calc,Delta,GiB,
megatron-22B,|,1.42,1.40,1.72%,48.15,|,1.1,1.14,-3.33%,52.08,
gpt3-175B,|,18.13,18.03,0.56%,48.10,|,13.75,13.64,0.81%,54.07,
turing-530B,|,49.05,49.89,-1.72%,42.27,|,37.83,34.47,8.87%,53.54,
megatron-1T,|,94.42,90.08,4.60%,46.27,|,71.49,66.04,7.62%,59.15,
Ave,,3.65%
Max,,8.87%
,



### Testing llm-optimal-execution (float16) (using -f)
Total executions: 3648
Good executions: 352
Bad executions: 3296
Calculation rate: 1799.28 calcs/sec
Best sample rate: 240.8057353728293
Output: /tmp/calculon_530B_fp16.json


### Testing llm-optimal-execution (float8) (using -m)
Total executions: 8832
Good executions: 1760
Bad executions: 7072
Calculation rate: 2125.52 calcs/sec
Best sample rate: 519.9576573764684
Output: /tmp/calculon_530B_fp8.csv.gz



### Testing llm-all-executions (float8)
Total executions: 10944
Good executions: 1760
Bad executions: 9184
Calculation rate: 2219.51 calcs/sec
Output: /tmp/calculon_530B_fp8_all.csv.gz



