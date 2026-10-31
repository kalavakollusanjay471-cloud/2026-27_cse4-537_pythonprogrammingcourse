# Examination Result and Grace-Mark Validation – Python Program

## 1. Problem Statement

Develop a Python program to process examination results across multiple subjects. The program should calculate total marks, check subject-wise pass criteria, apply grace marks according to a specified policy, and generate the final student classification.

The program should:

1. Accept the student's name and number of subjects.
2. Input subject names, obtained marks, and maximum marks.
3. Check the minimum passing marks for each subject.
4. Apply grace marks to students who fail by a small margin.
5. Ensure grace marks do not exceed the maximum marks.
6. Calculate total marks and percentage.
7. Classify students as Distinction, First Class, Second Class, Pass, or Fail.
8. Display the final examination result.

## 2. Algorithm

1. Start the program.
2. Enter the student's name.
3. Enter the number of subjects.
4. Enter the maximum marks and passing marks.
5. Enter the grace-mark limit per subject.
6. For each subject:
   - Enter subject name.
   - Enter obtained marks.
   - Validate marks.
   - Check whether the student has passed.
   - If the student fails within the grace-mark limit, apply grace marks.
   - Ensure final marks do not exceed maximum marks.
7. Calculate total obtained marks.
8. Calculate total maximum marks.
9. Calculate percentage.
10. Check whether the student passed all subjects.
11. Assign the final classification.
12. Display the examination result.
13. Stop the program.

## 3. Flowchart


```

flowchart TD
    A([Start]) --> B[/Enter student name and subject count/]
    B --> C[/Enter maximum marks, pass marks and grace limit/]
    C --> D{Valid examination rules?}
    D -- No --> E[Display Invalid Rules]
    E --> Z([Stop])
    D -- Yes --> F[/Enter subject name and obtained marks/]
    F --> G{Marks valid?}
    G -- No --> H[Display Invalid Marks]
    H --> Z
    G -- Yes --> I{Marks below pass marks?}
    I -- No --> J[Keep original marks]
    I -- Yes --> K{Required grace within limit?}
    K -- Yes --> L[Apply grace marks]
    K -- No --> M[Keep original marks]
    L --> N[Ensure marks do not exceed maximum]
    J --> O{Final marks >= pass marks?}
    M --> O
    N --> O
    O -- No --> P[Mark subject as FAIL]
    O -- Yes --> Q[Mark subject as PASS]
    P --> R{More subjects?}
    Q --> R
    R -- Yes --> F
    R -- No --> S[Calculate total and percentage]
    S --> T{All subjects passed?}
    T -- No --> U[Classification = FAIL]
    T -- Yes --> V[Determine final classification]
    U --> W[Display final result]
    V --> W
    W --> Z
       
```

## 5. Sample Input

```
===== EXAMINATION RESULT SYSTEM =====

Enter student name: Sanjay
Enter number of subjects: 5
Enter maximum marks per subject: 100
Enter minimum passing marks: 40
Enter maximum grace marks per subject: 5

Subject 1
Enter subject name: Mathematics
Enter obtained marks: 85

Subject 2
Enter subject name: Physics
Enter obtained marks: 38

Subject 3
Enter subject name: Chemistry
Enter obtained marks: 75

Subject 4
Enter subject name: English
Enter obtained marks: 65

Subject 5
Enter subject name: Programming
Enter obtained marks: 90
```

## 6. Sample Output

```
===== FINAL EXAMINATION RESULT =====

Student Name: Sanjay

Subject-wise Results:
-----------------------------------------------
Subject | Original | Grace | Final | Status
-----------------------------------------------
Mathematics | 85 | 0 | 85 | PASS
Physics | 38 | 2 | 40 | PASS
Chemistry | 75 | 0 | 75 | PASS
English | 65 | 0 | 65 | PASS
Programming | 90 | 0 | 90 | PASS
-----------------------------------------------

Total Marks: 355 / 500
Grace Marks Used: 2
Percentage: 71.0 %
Final Classification: FIRST CLASS

===== RESULT COMPLETED =====
```

## 7. Mermaid Flowchart Code

\#chatgpt-mermaid-\_r_gb\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(237, 237, 237);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_gb\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_gb\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_gb\_ .error-icon{fill:rgb(48, 48, 48);}#chatgpt-mermaid-\_r_gb\_ .error-text{fill:rgb(237, 237, 237);stroke:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_gb\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_gb\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_gb\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_gb\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_gb\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_gb\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_gb\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_gb\_ .marker.cross{stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_gb\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_gb\_ p{margin:0;}#chatgpt-mermaid-\_r_gb\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_gb\_ .cluster-label text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_gb\_ .cluster-label span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_gb\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_gb\_ .label text,#chatgpt-mermaid-\_r_gb\_ span{fill:rgb(237, 237, 237);color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_gb\_ .node rect,#chatgpt-mermaid-\_r_gb\_ .node circle,#chatgpt-mermaid-\_r_gb\_ .node ellipse,#chatgpt-mermaid-\_r_gb\_ .node polygon,#chatgpt-mermaid-\_r_gb\_ .node path{fill:rgb(9, 23, 44);stroke:rgb(31, 78, 148);stroke-width:1px;}#chatgpt-mermaid-\_r_gb\_ .rough-node .label text,#chatgpt-mermaid-\_r_gb\_ .node .label text,#chatgpt-mermaid-\_r_gb\_ .image-shape .label,#chatgpt-mermaid-\_r_gb\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_gb\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_gb\_ .rough-node .label,#chatgpt-mermaid-\_r_gb\_ .node .label,#chatgpt-mermaid-\_r_gb\_ .image-shape .label,#chatgpt-mermaid-\_r_gb\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_gb\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_gb\_ .root .anchor path{fill:rgb(175, 175, 175)!important;stroke-width:0;stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_gb\_ .arrowheadPath{fill:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_gb\_ .edgePath .path{stroke:rgb(175, 175, 175);stroke-width:1px;}#chatgpt-mermaid-\_r_gb\_ .flowchart-link{stroke:rgb(175, 175, 175);fill:none;}#chatgpt-mermaid-\_r_gb\_ .edgeLabel{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_gb\_ .edgeLabel p{background-color:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_gb\_ .edgeLabel rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_gb\_ .labelBkg{background-color:rgba(0, 0, 0, 0.5);}#chatgpt-mermaid-\_r_gb\_ .cluster rect{fill:rgb(48, 48, 48);stroke:rgba(255, 255, 255, 0.15);stroke-width:1px;}#chatgpt-mermaid-\_r_gb\_ .cluster text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_gb\_ .cluster span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_gb\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(48, 48, 48);border:1px solid rgba(255, 255, 255, 0.15);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_gb\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_gb\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_gb\_ .icon-shape,#chatgpt-mermaid-\_r_gb\_ .image-shape{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_gb\_ .icon-shape p,#chatgpt-mermaid-\_r_gb\_ .image-shape p{background-color:rgb(0, 0, 0);padding:2px;}#chatgpt-mermaid-\_r_gb\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_gb\_ .image-shape .label rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_gb\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_gb\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_gb\_ .node .neo-node{stroke:rgb(31, 78, 148);}#chatgpt-mermaid-\_r_gb\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_gb\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_gb\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_gb\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_gb\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_gb\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_gb\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_gb\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_gb\_ [data-look="neo"].node .neo-line path{stroke:rgb(31, 78, 148);filter:none;}#chatgpt-mermaid-\_r_gb\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_gb\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_gb\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_gb\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_gb\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_gb\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_gb\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_gb\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_gb\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_gb\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_gb\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_gb\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-width:1px;}#chatgpt-mermaid-\_r_gb\_ .node rect,#chatgpt-mermaid-\_r_gb\_ .node circle,#chatgpt-mermaid-\_r_gb\_ .node ellipse,#chatgpt-mermaid-\_r_gb\_ .node polygon,#chatgpt-mermaid-\_r_gb\_ .node path{fill:rgb(0, 40, 77);stroke:rgba(255, 255, 255, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_gb\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_gb\_ .mermaid-decision .label-container{fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_gb\_ .edgePaths .flowchart-link{stroke:rgb(175, 175, 175);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_gb\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_gb\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartEnter student name andsubject countEnter maximum marks, passmarks and grace limitValid examination rules?Display Invalid RulesStopEnter subject name andobtained marksMarks valid?Display Invalid MarksMarks below pass marks?Keep original marksRequired grace within limit?Apply grace marksKeep original marksEnsure marks do not exceedmaximumFinal marks = pass marks?Mark subject as FAILMark subject as PASSMore subjects?Calculate total and percentageAll subjects passed?Classification = FAILDetermine final classificationDisplay final resultNoYesNoYesNoYesYesNoNoYesYesNoNoYes

## 8. Important Formulas

| Calculation          | Formula                                   |
| -------------------- | ----------------------------------------- |
| Required Grace Marks | Pass Marks − Obtained Marks               |
| Final Marks          | Obtained Marks + Grace Marks              |
| Total Marks          | Sum of Final Subject Marks                |
| Percentage           | (Total Marks / Maximum Total Marks) × 100 |
| Grace Limit          | Grace Marks ≤ Allowed Grace Limit         |

Classification rules used in this program:

| Percentage                      | Classification |
| ------------------------------- | -------------- |
| 75% and above                   | Distinction    |
| 60% – 74.99%                    | First Class    |
| 50% – 59.99%                    | Second Class   |
| Below 50% (all subjects passed) | Pass           |
| Any subject failed              | Fail           |

## 9. Expected Result

- Processes marks for multiple subjects.
- Checks subject-wise passing criteria.
- Applies grace marks when eligible.
- Prevents marks from exceeding maximum marks.
- Calculates total marks and percentage.
- Generates the final examination classification.

Note: This program uses an example grace-mark policy of up to 5 marks per subject. Actual grace-mark rules may differ depending on university examination regulations.
