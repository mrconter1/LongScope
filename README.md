# LongScope: Assessing Contextual Comprehension in Large Language Models

## Overview

LongScope is a modest yet comprehensive benchmark designed to test and evaluate the capacity of large language models (LLMs) in managing long contextual dependencies. In the realm of natural language processing, retaining and applying information from extended contexts remains a significant challenge for LLMs. LongScope aims to assess the capability of these models to intelligently process and integrate information dispersed across extensive textual segments, advancing beyond simple sentence extraction or retrieval.

## Motivation

With recent advancements, LLMs have seen a substantial increase in context length capabilities. Nevertheless, the effectiveness of these models in handling longer contexts warrants in-depth exploration and understanding. LongScope provides a necessary framework for evaluating long context processing in LLMs, contributing to the field's progress.

## Key Features

- **Diverse Prompt Generation:** Facilitates the generation of varied prompts, including shorter lengths where current LLMs excel and longer spans that pose more significant challenges.
- **Intelligent Reasoning Evaluation:** Centers on assessing the LLM's ability to perform intelligent reasoning over an extended context.
- **Flexible and Scalable:** Designed for easy modification and enhancement to incorporate more complex question types and scenarios.

## How It Works

LongScope generates a series of facts, each linked to an entity and an emotion, uniformly distributed across a text. It then poses questions requiring the LLM to identify specific facts from different context parts to provide accurate answers. This method tests the LLM's effectiveness in handling and integrating information from various context segments.

## Usage

1. **Fact Generation:** Randomly generates a set number of facts, each with an associated entity and emotion.
2. **Question Formulation:** Creates questions of varying complexity, requiring identification of specific facts from the context.
3. **Evaluation:** Assesses the LLM's performance based on its ability to accurately answer questions by effectively extracting and integrating context information.

## Example Output

```
KJWDRQRCKHTOO is angry
FEKUVFUNMQLBFQP is sad
XUSKLV is happy
QBMQRBZDKE is happy
RCPZXFQAMPA is happy
WYJCWMDZLXHWY is happy
WHLALHNO is happy
LLEHJOEDE is angry
RQJAJMYXSQ is angry
RHTRLUDNGLHO is happy

Question: Are none of KJWDRQRCKHTOO, WHLALHNO, RQJAJMYXSQ happy?
//Answer: False
```

## Contributions and Future Work

Created in approximately 1.5 hours, LongScope suggest an alternative approach towards more sophisticated benchmarks in this domain. Future work could involve:

- More complex question formulations.
- Studies on the correlation between context length and LLM performance.

## Getting Started

To use LongScope, clone the repository and follow the setup instructions in the documentation. Sample scripts and usage examples are provided for easy implementation in LLM evaluations.

## Acknowledgments and Contributions

LongScope was hastily put together, but we actively encourage feedback, suggestions, and contributions. Whether you're a researcher, practitioner, or enthusiast in natural language processing and artificial intelligence, your input and collaboration are highly valued.
