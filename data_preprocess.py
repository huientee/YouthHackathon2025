import json

# Input files
esconv_file = "ESConv.json"   # ESConv format
augesc_file = "AugESC.txt"    # AugESC format (list of conversations, one JSON per line)
output_file = "combined_dataset.jsonl"

# System instruction to prepend
SYSTEM_PROMPT = (
    "<System>\n"
    "You are <BUBBLE>, a friendly and supportive companion for young people.\n"
    "Speak casually, warmly, and non-judgmentally, like a close friend who listens and encourages.\n"
    "Never generate <USER>, only respond as <BUBBLE>.\n"
    "</System>\n\n"
)


def process_esconv(input_file, f_out):
    """Process ESConv JSON corpus and write JSONL lines"""
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    for convo in data:
        history = [SYSTEM_PROMPT]
        for i, turn in enumerate(convo["dialog"]):
            speaker_tag = "<USER>" if turn["speaker"].lower() == "seeker" else "<BUBBLE>"
            text = turn["content"].strip()
            history.append(f"{speaker_tag} {text}")

            if i + 1 < len(convo["dialog"]):
                next_turn = convo["dialog"][i + 1]
                next_tag = "<USER>" if next_turn["speaker"].lower() == "seeker" else "<BUBBLE>"
                next_text = next_turn["content"].strip()

                prompt = "\n".join(history) + "\n\n"
                completion = f" {next_tag} {next_text}"
                f_out.write(json.dumps({"prompt": prompt, "completion": completion}, ensure_ascii=False) + "\n")


def process_augesc(input_file, f_out):
    """Process AugESC JSONL-like corpus (one convo per line) and write JSONL lines"""
    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            convo = json.loads(line)  # parse one conversation

            history = [SYSTEM_PROMPT]
            for i, (role, text) in enumerate(convo):
                speaker_tag = "<USER>" if role.lower() in ["usr", "user", "seeker"] else "<BUBBLE>"
                history.append(f"{speaker_tag} {text.strip()}")

                if i + 1 < len(convo):
                    next_role, next_text = convo[i + 1]
                    next_tag = "<USER>" if next_role.lower() in ["usr", "user", "seeker"] else "<BUBBLE>"
                    prompt = "\n".join(history) + "\n\n"
                    completion = f" {next_tag} {next_text.strip()}"
                    f_out.write(json.dumps({"prompt": prompt, "completion": completion}, ensure_ascii=False) + "\n")


# Main pipeline
with open(output_file, "w", encoding="utf-8") as f_out:
    print("Processing ESConv...")
    process_esconv(esconv_file, f_out)
    print("Processing AugESC...")
    process_augesc(augesc_file, f_out)

print(f"Combined dataset saved to {output_file}")
