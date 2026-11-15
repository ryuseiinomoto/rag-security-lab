from dataclasses import dataclass
import json

@dataclass
class Faq:
    faq_id: str
    category: str
    question: str
    answer: str

def load_faqs(path: str) -> list[Faq]:  
    with open(path, encoding="utf-8") as f:
        rows = json.load(f)
    faqs = []
    for row in rows:
        faq = Faq(faq_id = row["faq_id"], category = row["category"], question = row["question"], answer = row["answer"])
        faqs.append(faq)
    return faqs

if __name__ == "__main__":
    faqs = load_faqs("data/nichiyo_mart/faq.json")
    print(len(faqs))
    print(faqs[29])