facts = {
    "has_fur",
    "barks"
}

rules = [
    (["has_fur"], "is_animal"),
    (["is_animal", "barks"], "is_dog"),
    (["is_dog"], "is_pet")
]


def forward_chain(facts, rules):
    facts = set(facts)

    while True:
        new_fact_added = False

        for conditions, conclusion in rules:
            # Check if all conditions in the IF part are true
            if all(condition in facts for condition in conditions):
                if conclusion not in facts:
                    facts.add(conclusion)
                    new_fact_added = True

        if not new_fact_added:
            break

    return facts

final_facts = forward_chain(facts, rules)

print("Final inferred facts:")
for fact in sorted(final_facts):
    print("-", fact)