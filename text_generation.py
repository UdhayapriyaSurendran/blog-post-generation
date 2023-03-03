from aitextgen import aitextgen

ai = aitextgen()



def generator(prompt_txt, length):
    generated_txt = ai.generate_one(prompt=prompt_txt, max_length=length)
    return generated_txt



