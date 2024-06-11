# VT_thesis

This is the acompanying repository for my master's thesis paper in Voice Technology at the University of Groningen/Campus Fryslan: **Addressing ASR Bias Against Foreign-Accented Dutch: A Synthetic Data Approach**.
Submitted on June 11th, 2024.

The paper can be found at (thesis repo link).

## Abstract
Despite substantial improvements in automatic speech recognition (ASR) over the last years, the high performance achieved for ”standard speakers” does not hold across all genders, ages, or foreign accents. As a result, an important area of research is inclusive ASR, aimed at reducing the performance gaps such systems display across subgroups of the population. In the present thesis, I evaluate one of the most recent and robust ASR systems (OpenAI’s Whisper) to uncover and assess the level of bias it displays against foreign-accented Dutch. Additionally, I investigate whether synthetically accented speech samples obtained from a fine-tuned speech synthesis model (FastSpeech2) can act as a viable data augmentation tool to create additional training data for Whisper, in a fine-tuning transfer learning paradigm. By investigating bias, as opposed to WER reduction, I specifically pay attention to both the improvement in performance on foreign-accented Dutch and the potential decrease in performance on native Dutch. Experimental results show that fine-tuning Whisper on synthetic accented speech data does increase its performance on natural speech samples, although this comes at the cost of decreased performance on native samples after fine-tuning. Additionally, the insights from fine-tuning Whisper put into question its suitability for this learning paradigm, as its large number of parameters displays increased stability on small, low-resource datasets.

## Repo structure
Various files I have used to reach my results can be found here, related both to the FastSpeech2 part and to the Whisper part. Most importantly, the notebooks I've used for fine-tuning whisper can be found in the whisper-related folder and contain the hyperparameters defined for training.

## Data sources and fine-tuned checkpoints
Most of the data I have used and all the fine-tuned model checkpoints are saved to my [HuggingFace](https://huggingface.co/mariatepei) for convenience. The CSS10 dataset of native Dutch speech can be found [here](https://github.com/Kyubyong/css10/tree/master).

## Acknowledgments
The FastSpeech 2 implementation I've used is [here](https://github.com/ming024/FastSpeech2).
In figuring out how to fine-tune Whisper on a custom dataset, important insights came from [Sanchit's bolgpost](https://huggingface.co/blog/fine-tune-whisper#closing-remarks) and [Trelis Research YouTube videos](https://www.youtube.com/@TrelisResearch).
