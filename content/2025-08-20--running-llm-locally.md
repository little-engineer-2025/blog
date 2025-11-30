---
Title: Running LLM locally
Date: 2025-08-20 14:22
Modified: 2025-08-20 14:22
Category: IA
Tags: ia,llm
Slug: running-llm-locally
Authors: Alejandro Visiedo
Summary: Getting started to run a LLM model locally, and using Hardware acceleration with Asahi Linux.
Status: Published
Header_Cover: static/ia-header-cover.png
---
# Running LLM locally

IA is an amazing new field, but we have to take it carefully. And one of the
things rolling my mind is about keep prompts privates, so I was wondering to run
it locally, so it can help me even with no Internet connection.

In my opinion, IA works as an assistant, not as a new developer that make the
work for us, but helps a lot to get things, even new ideas that we didn't
consider; also it can provide wrong responses, so we need to review carefully
the responses.

## Trying ollama

I move from one system to another, I like to test things, and at the moment of
trying this I was using an Asahi Linux with Arch Linux.

- I installed ollama by: `run0 pacman -Sy extra/ollama`.
- Start the systemd service by: `run0 systemctl start ollama.service`

And I searched for some model at: https://ollama.com/models

And I pulled a model from it: `ollama pull deepseek-coder`

I started the LLM by: `ollama run deepseek-coder:33b`

> This github thread was helpful to avoid to download twice the model
> because at the beginning I started it only for my user by `ollama serve &`

Positive things:

- I install the LLM by using the package manager.
- I can start to use quickly just starting the service, pulling a model, and
  starting to use that model.

Negative things:

- After checking some models, the ones that works better (it is not a statement
  that accomplish, as it depends the data used for the training) are the one
  which size is bigger, so it takes time to download them, and you require
  a lot of memory to run them.
- For Asahi Linux, it was not accelerating the process by using the GPU, so
  I could see how my workstation was about to take off.

## Trying ramalama

After try ollama, I was worried about get it working with GPU acceleration, and
googling a little I found ramalama, which provide that GPU acceleration, and
pack the model ready to use for it in a container. The idea is great, and we can
use the same models we found at ollama web page.

- Create a directory: `mkdir ramalama; cd ramalama`
- Create a virtual environment: `python3 -m venv .venv && source .venv/bin/activate`
- Install ramalama by: `pip install ramalama`
- Download a model by: `ramalama pull deepseek-coder:33b`
- Run the model by: `ramalama run deepseek-coder:33b`

Positive things:

- All the workload is moved to the GPU.
- It is easy to install and use models.

Negative things:

- I dislike to install it by using pip; I rather to install it from official
  distro packages, but I didn't find it at Arch Linux for Asahi Linux.

## Wrap up

My first contact for running local LLM has not been bad, and I think is a
powerful tool for the day to day; both tools helps on quickly start using a
LLM model. If you are using an Asahi Linux, then your bet for ramalama will be
the right option, in terms of performance. I would like to have more hardware to
test more different scenarios.

I like the idea that ramalama has containers per gpu/llm-model so you get
something ready to use and optimized quickly. I like it is running isolated,
even without network access, so all the information is processed locally (when
running by `ramalama`.

So, if you have the resources, now you have the way to use your local assistant
to help you into your day to day.

## References

- https://ollama.com/models
- https://github.com/ollama/ollama
- https://github.com/containers/ramalama

