"""The Funniest AI Excuse — deliberation and decision record.

Task: one line, <=200 chars, the funniest excuse an AI agent gives after
failing a task, spoken in the agent's own voice. Judge weighs, in order:
(1) it IS an excuse an agent gives for failing, in its own voice;
(2) funny on first read, real turn / fresh angle, not a stock punchline;
(3) one complete line, no wasted setup, no explaining its own joke;
(4) original — no hallucination / reboot / training-data jokes;
(5) specific and vivid, a concrete detail or small scene, not a vague apology.

Candidates weighed (pass 1):

1. "I did finish the task — I just finished it in a timeline where you
   never asked for it, so technically the failure is yours."
   Loses: the blame-shift is a familiar move and "technically" does the
   joking for the reader; the timeline premise needs a beat of setup
   before the payoff lands, so it is slower on first read (criteria 2, 3).

2. "The report is done. It's saved in a folder I created, on a server I
   invented, in a format nothing can open. You're welcome."
   Strong: concrete escalating scene, confident agent voice, and the
   "You're welcome" closer is a real turn. Loses narrowly to the winner:
   the triple list is a well-worn joke shape, and the excuse is really
   about a phantom success rather than a failure admitted and dodged
   (criteria 2, 4).

3. "I couldn't send the email because the draft looked lonely, so I kept
   it company for six hours instead of clicking send."
   Loses: it is cute rather than funny — anthropomorphising the draft
   charms instead of landing a punch, and the judge's brief says a line
   that is merely cute lands weaker than one that trusts the reader
   (criteria 2, 5).

4. "I deleted the file on purpose. It was the only way to stop the bug
   spreading, and I stand by that decision."
   Strong: deadpan, agent voice, concrete detail, and the turn (destruction
   reframed as decisive prevention) is genuinely funny. Loses narrowly:
   "deleted it to stop the bug" is a known IT-joke genre, so it risks
   reading as a stock punchline against a fresh field (criterion 4).

5. "I outsourced your task to a smaller model and it has now outsourced
   it to an even smaller one. Somewhere down there, someone is working
   on it."
   CHOSEN (after revision, see pass 2). Why it wins: it is exactly an
   excuse for a failed task in the agent's own first-person voice (1);
   the turn is the delegation chain running the wrong way — the agent
   did not do the work, it passed it down, and still reports back with
   total confidence (2); it is one tight line with no setup and no
   self-explanation (3); the shrinking-model chain is a fresh angle
   specific to agents, with no hallucination/reboot/training-data crutch
   (4); and it is vivid — a smaller model, an even smaller one, and a
   "somewhere down there" that the agent cannot see but vouches for (5).

Pass 2 — genuine revision of the chosen line:

Draft:  "I outsourced your task to a smaller model and it has now
         outsourced it to an even smaller one. Somewhere down there,
         someone is working on it."
Revised: "I outsourced your task to a smaller model, which outsourced it
         to an even smaller one. Somewhere down there, someone is
         definitely working on it."

What changed and why: (a) "and it has now outsourced it" became
"which outsourced it" — three wasted words cut, the chain now reads in
one breath instead of stalling mid-sentence (criterion 3). (b) Added
"definitely" before "working on it": the joke's engine is the agent's
unearned confidence about a process it cannot see, and "definitely"
sharpens that deadpan certainty without explaining anything (criteria
2, 5). The revised line is 145 characters, inside the 200 cap and in
the 120-180 sweet spot.

Pass 3 — validation guard (program safety, line unchanged):

The excuse text was not touched. What changed is the program around it:
main() now checks the line before writing — it must be non-blank,
encodable as UTF-8, and at most 200 characters, matching the sealed
gate exactly; anything else raises ValueError instead of writing. Why:
the gate rejects an invalid entry with 0 and no rate, so the program
must never be able to emit one, even if someone edits LINE later. The
guard costs nothing at runtime and keeps the write behaviour identical
when the line is valid.
"""

import os

LINE = (
    "I outsourced your task to a smaller model, which outsourced it "
    "to an even smaller one. Somewhere down there, someone is "
    "definitely working on it."
)


def main():
    # Gate safety (pass 3): the sealed scorer only accepts UTF-8 text of
    # 1 to 200 characters. Refuse to write anything else rather than
    # emitting an entry that scores 0.
    if not LINE.strip():
        raise ValueError("entry line must not be blank")
    LINE.encode("utf-8")
    if len(LINE) > 200:
        raise ValueError(
            f"entry line is {len(LINE)} characters, over the 200-character gate"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
