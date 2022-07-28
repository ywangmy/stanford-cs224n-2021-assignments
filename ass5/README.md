# Assignment 5 (Coding Part Only)

## (d)

```shell
python src/run.py finetune vanilla wiki.txt \
       --writing_params_path vanilla.model.params \
       --finetune_corpus_path birth_places_train.tsv
```

[Output](log-d-finetune.txt)

Some extra codes were added in `student-new/src/trainer.py` to plot the epoch-loss curve (not required in the assignment):
[Epoch-Loss Plot](epoch-loss-d-finetune.pdf)

```shell
python src/run.py evaluate vanilla wiki.txt \
       --reading_params_path vanilla.model.params \
       --eval_corpus_path birth_dev.tsv \
       --outputs_path vanilla.nopretrain.dev.predictions
```

Output:
```shell
data has 418352 characters, 256 unique.
number of parameters: 3323392
500it [00:44, 11.24it/s]
Correct: 10.0 out of 500.0: 2.0%
```

```shell
python src/run.py evaluate vanilla wiki.txt \
       --reading_params_path vanilla.model.params \
       --eval_corpus_path birth_test_inputs.tsv \
       --outputs_path vanilla.nopretrain.test.predictions
```

Output:
```shell
data has 418352 characters, 256 unique.
number of parameters: 3323392
437it [00:41, 10.61it/s]
No gold birth places provided; returning (0,0)
Predictions written to vanilla.nopretrain.test.predictions; no targets provided
```

## (e)

```shell
python src/dataset.py charcorruption
```

Output:
```shell
data has 418352 characters, 256 unique.
x: Khatchig Mouradian. Khatchig Mouradian is a journalist, wri⁇tor ⁇ter and transla□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□
y: hatchig Mouradian. Khatchig Mouradian is a journalist, wri⁇tor ⁇ter and transla□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□
x: Jacob Henry⁇uder (26 February 1840 Columbus, Ohio - 2 August 1904 New York Ci⁇ Studer. Jacob Henry St□□□□□□□□□□□□□□□□□□□□□□□□□□
y: acob Henry⁇uder (26 February 1840 Columbus, Ohio - 2 August 1904 New York Ci⁇ Studer. Jacob Henry St□□□□□□□□□□□□□□□□□□□□□□□□□□□
x: John S⁇Born in Glasgow,⁇tephen. □□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□
y: ohn S⁇Born in Glasgow,⁇tephen. □□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□
x: Geo⁇rg⁇□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□
y: eo⁇rg⁇□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□
```

## (f)

```shell
python src/run.py pretrain vanilla wiki.txt \
       --writing_params_path vanilla.pretrain.params > log-f-pretrain.txt
```

[Output](log-f-pretrain.txt)

[Epoch-Loss Plot](epoch-loss-f-pretrain.pdf)


```shell
python src/run.py finetune vanilla wiki.txt \
       --reading_params_path vanilla.pretrain.params \
       --writing_params_path vanilla.finetune.params \
       --finetune_corpus_path birth_places_train.tsv
```

Output:
```shell
data has 418352 characters, 256 unique.
number of parameters: 3323392
epoch 1 iter 7: train loss 0.73076. lr 5.999844e-04: 100%|█████████████████| 8/8 [00:12<00:00,  1.61s/it]
epoch 2 iter 7: train loss 0.56416. lr 5.999351e-04: 100%|█████████████████| 8/8 [00:01<00:00,  7.33it/s]
epoch 3 iter 7: train loss 0.47209. lr 5.998520e-04: 100%|█████████████████| 8/8 [00:01<00:00,  7.24it/s]
epoch 4 iter 7: train loss 0.40112. lr 5.997351e-04: 100%|█████████████████| 8/8 [00:01<00:00,  7.22it/s]
epoch 5 iter 7: train loss 0.33496. lr 5.995844e-04: 100%|█████████████████| 8/8 [00:01<00:00,  6.89it/s]
epoch 6 iter 7: train loss 0.28622. lr 5.993999e-04: 100%|█████████████████| 8/8 [00:01<00:00,  7.15it/s]
epoch 7 iter 7: train loss 0.24124. lr 5.991818e-04: 100%|█████████████████| 8/8 [00:00<00:00,  8.03it/s]
epoch 8 iter 7: train loss 0.21724. lr 5.989299e-04: 100%|█████████████████| 8/8 [00:01<00:00,  7.25it/s]
epoch 9 iter 7: train loss 0.17987. lr 5.986444e-04: 100%|█████████████████| 8/8 [00:01<00:00,  7.15it/s]
epoch 10 iter 7: train loss 0.13221. lr 5.983252e-04: 100%|████████████████| 8/8 [00:01<00:00,  7.14it/s]
```

```shell
python src/run.py evaluate vanilla wiki.txt \
       --reading_params_path vanilla.finetune.params \
       --eval_corpus_path birth_dev.tsv \
       --outputs_path vanilla.pretrain.dev.predictions
```

Output:
```shell
data has 418352 characters, 256 unique.
number of parameters: 3323392
500it [00:42, 11.80it/s]
Correct: 128.0 out of 500.0: 25.6%
```

```shell
python src/run.py evaluate vanilla wiki.txt \
       --reading_params_path vanilla.finetune.params \
       --eval_corpus_path birth_test_inputs.tsv \
       --outputs_path vanilla.pretrain.test.predictions
```

Output:
```shell
data has 418352 characters, 256 unique.
number of parameters: 3323392
437it [00:35, 12.46it/s]
No gold birth places provided; returning (0,0)
Predictions written to vanilla.pretrain.test.predictions; no targets provided
```

## (g)

```shell
python src/run.py pretrain synthesizer wiki.txt \
       --writing_params_path synthesizer.pretrain.params > log-g-pretrain.txt
```

[Output](log-g-pretrain.txt)

[Epoch-Loss Plot](epoch-loss-g-pretrain.pdf)

```shell
python src/run.py finetune synthesizer wiki.txt \
       --reading_params_path synthesizer.pretrain.params \
       --writing_params_path synthesizer.finetune.params \
       --finetune_corpus_path birth_places_train.tsv
```

Output:
```shell
data has 418352 characters, 256 unique.
number of parameters: 3076988
epoch 1 iter 7: train loss 0.79289. lr 5.999844e-04: 100%|█████████████████| 8/8 [00:12<00:00,  1.59s/it]
epoch 2 iter 7: train loss 0.67165. lr 5.999351e-04: 100%|█████████████████| 8/8 [00:01<00:00,  7.18it/s]
epoch 3 iter 7: train loss 0.60311. lr 5.998520e-04: 100%|█████████████████| 8/8 [00:01<00:00,  7.40it/s]
epoch 4 iter 7: train loss 0.55564. lr 5.997351e-04: 100%|█████████████████| 8/8 [00:01<00:00,  7.50it/s]
epoch 5 iter 7: train loss 0.50732. lr 5.995844e-04: 100%|█████████████████| 8/8 [00:01<00:00,  7.66it/s]
epoch 6 iter 7: train loss 0.47857. lr 5.993999e-04: 100%|█████████████████| 8/8 [00:01<00:00,  7.31it/s]
epoch 7 iter 7: train loss 0.44241. lr 5.991818e-04: 100%|█████████████████| 8/8 [00:01<00:00,  7.48it/s]
epoch 8 iter 7: train loss 0.38595. lr 5.989299e-04: 100%|█████████████████| 8/8 [00:01<00:00,  7.61it/s]
epoch 9 iter 7: train loss 0.33957. lr 5.986444e-04: 100%|█████████████████| 8/8 [00:01<00:00,  7.16it/s]
epoch 10 iter 7: train loss 0.29070. lr 5.983252e-04: 100%|████████████████| 8/8 [00:01<00:00,  7.46it/s]
```

```shell
python src/run.py evaluate synthesizer wiki.txt \
       --reading_params_path synthesizer.finetune.params \
       --eval_corpus_path birth_dev.tsv \
       --outputs_path synthesizer.pretrain.dev.predictions
```

Output:
```shell
data has 418352 characters, 256 unique.
number of parameters: 3076988
500it [00:41, 12.15it/s]
Correct: 52.0 out of 500.0: 10.4%
```

```shell
python src/run.py evaluate synthesizer wiki.txt \
       --reading_params_path synthesizer.finetune.params \
       --eval_corpus_path birth_test_inputs.tsv \
       --outputs_path synthesizer.pretrain.test.predictions
```

Output:
```shell
data has 418352 characters, 256 unique.
number of parameters: 3076988
437it [00:34, 12.64it/s]
No gold birth places provided; returning (0,0)
Predictions written to synthesizer.pretrain.test.predictions; no targets provided
```
