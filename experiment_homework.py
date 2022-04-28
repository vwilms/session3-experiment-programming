import pandas as pd
from psychopy import core, visual, event

stimuli = pd.read_csv('lexical_decision_stimuli.csv')
stimuli = stimuli.sample(frac=1)

window = visual.Window()
text_stim = visual.TextStim(window)

instruction = visual.TextStim(window)

instruction.text = "Welkom bij dit experiment! Druk op de toets 'A' voor de woorden en op de toets 'L' voor de non-woorden.\n\nDruk op de spatiebalk om te beginnen."
instruction.draw()
window.flip()
event.waitKeys(keyList=['space'])

for count_num in [5,4,3,2,1]:
    instruction.text = count_num
    instruction.draw()
    window.flip()
    core.wait(1)

results = []

for index, current_trial in stimuli.iterrows():
    text_stim.text = current_trial[3]
    text_stim.draw()
    window.flip()
    clock = core.Clock()
    keys = event.waitKeys(maxWait=5, keyList=['a', 'l'], timeStamped=clock, clearEvents=True)
    if keys is not None:
        pressed = keys[0][0]
        rt = keys[0][1]
    else:
        pressed = None
        rt = core.Clock()

    results.append({
            'reaction_time': rt,
            'key': pressed,
            'word': current_trial[3],
            'freq': current_trial[2]
        })

results = pd.DataFrame(results)
results.to_csv('ppt1_output.csv', index_label=0)

window.close()
core.quit()