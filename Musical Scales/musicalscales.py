jumps=[2,4,5,7,9,11,12]
notes=["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
scales={notes[i]:{notes[(i+j)%len(notes)] for j in jumps}for i in range(len(notes))}
n=input()
s=set(input().split())
res=" ".join(filter(lambda z: s.issubset(scales[z]),notes))
print(res if len(res)>0 else 'none')
