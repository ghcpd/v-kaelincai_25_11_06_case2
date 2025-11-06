# Project Flow Diagram

## 📊 Execution Flow

```
START
  │
  ├─> verify_structure.ps1 (Optional but recommended)
  │     │
  │     └─> ✓ All files present
  │
  ├─> run_all.ps1 (Master Script)
  │     │
  │     ├─> STEP 1: Project A (Pre-Enhancement)
  │     │     │
  │     │     ├─> setup.ps1
  │     │     │     └─> Create venv
  │     │     │     └─> Install dependencies
  │     │     │
  │     │     ├─> run_tests.ps1
  │     │     │     ├─> pytest tests/test_pre_ui.py
  │     │     │     │     ├─> TC001: ❌ FAIL (overlap)
  │     │     │     │     ├─> TC002: ❌ FAIL (overlap)
  │     │     │     │     ├─> TC003: ❌ FAIL (overlap)
  │     │     │     │     ├─> TC004: ❌ FAIL (overlap)
  │     │     │     │     ├─> TC005: ✅ PASS (error handling)
  │     │     │     │     └─> TC006: ❌ FAIL (overlap)
  │     │     │     │
  │     │     │     ├─> Generate charts (with overlaps)
  │     │     │     │     └─> results/charts/*.png
  │     │     │     │
  │     │     │     └─> Save results
  │     │     │           └─> results/results_pre.json
  │     │     │           └─> logs/log_pre.txt
  │     │     │
  │     │     └─> Expected: 1/6 tests pass (16.7%)
  │     │
  │     ├─> STEP 2: Project B (Post-Enhancement)
  │     │     │
  │     │     ├─> setup.ps1
  │     │     │     └─> Create venv
  │     │     │     └─> Install dependencies (+ adjustText)
  │     │     │
  │     │     ├─> run_tests.ps1
  │     │     │     ├─> pytest tests/test_post_ui.py
  │     │     │     │     ├─> TC001: ✅ PASS (no overlap)
  │     │     │     │     ├─> TC002: ✅ PASS (adaptive fonts)
  │     │     │     │     ├─> TC003: ✅ PASS (smart positioning)
  │     │     │     │     ├─> TC004: ✅ PASS (staggered labels)
  │     │     │     │     ├─> TC005: ✅ PASS (error handling)
  │     │     │     │     └─> TC006: ✅ PASS (number formatting)
  │     │     │     │
  │     │     │     ├─> Generate enhanced charts
  │     │     │     │     └─> results/charts/*_enhanced.png
  │     │     │     │
  │     │     │     └─> Save results
  │     │     │           └─> results/results_post.json
  │     │     │           └─> logs/log_post.txt
  │     │     │
  │     │     └─> Expected: 6/6 tests pass (100%)
  │     │
  │     └─> STEP 3: Generate Comparison Report
  │           │
  │           ├─> Load results_pre.json
  │           ├─> Load results_post.json
  │           ├─> Compare metrics
  │           ├─> Embed screenshots
  │           └─> Generate compare_report.md
  │
  └─> END
        │
        └─> Review Outputs:
              ├─> compare_report.md (comparison)
              ├─> Project_A_PreFeature_UI/results/ (pre-charts + JSON)
              └─> Project_B_PostFeature_UI/results/ (post-charts + JSON)
```

---

## 🏗️ Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    Test Data (Shared)                       │
│                   test_data.json                            │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ TC001: Normal bar chart (5 points)                   │  │
│  │ TC002: High-density chart (15 points)                │  │
│  │ TC003: Similar values (85-89)                        │  │
│  │ TC004: Multi-series (3 series × 4 categories)        │  │
│  │ TC005: Missing/null labels                           │  │
│  │ TC006: Large values (millions)                       │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                              │
                    ┌─────────┴─────────┐
                    │                   │
                    ▼                   ▼
    ┌───────────────────────┐  ┌───────────────────────┐
    │   Project A (Pre)     │  │   Project B (Post)    │
    │   Pre-Enhancement     │  │   Post-Enhancement    │
    └───────────────────────┘  └───────────────────────┘
                │                          │
    ┌───────────┴───────────┐  ┌───────────┴───────────┐
    │                       │  │                       │
    ▼                       ▼  ▼                       ▼
┌─────────┐           ┌─────────┐  ┌─────────┐
│  src/   │           │ tests/  │  │  src/   │  │ tests/  │
│ chart_  │           │test_pre_│  │ chart_  │  │test_post│
│generator│           │ ui.py   │  │generator│  │ ui.py   │
│  .py    │           │         │  │  .py    │  │         │
│         │           │         │  │         │  │         │
│ Static  │───generates─>Charts │  │ Dynamic │──generates──>Charts │
│ Labels  │           │ with    │  │ Labels  │  │ without │
│ (broken)│           │ overlaps│  │ (fixed) │  │ overlaps│
└─────────┘           └────┬────┘  └─────────┘  └────┬────┘
                           │                          │
                           ▼                          ▼
                    ┌─────────────┐          ┌─────────────┐
                    │  Results:   │          │  Results:   │
                    │ - Charts    │          │ - Charts    │
                    │ - JSON      │          │ - JSON      │
                    │ - Logs      │          │ - Logs      │
                    │ Pass: 1/6   │          │ Pass: 6/6   │
                    └──────┬──────┘          └──────┬──────┘
                           │                        │
                           └────────┬───────────────┘
                                    ▼
                      ┌──────────────────────────┐
                      │ generate_comparison_     │
                      │      report.py           │
                      └──────────┬───────────────┘
                                 ▼
                      ┌──────────────────────────┐
                      │   compare_report.md      │
                      │                          │
                      │ - Side-by-side charts    │
                      │ - Metrics comparison     │
                      │ - Improvement analysis   │
                      │ - Executive summary      │
                      └──────────────────────────┘
```

---

## 🔄 Data Flow

```
┌──────────────┐
│ test_data.   │
│   json       │
└──────┬───────┘
       │
       ├─────────────────────────────────────┐
       │                                     │
       ▼                                     ▼
┌─────────────────┐                  ┌─────────────────┐
│ Project A       │                  │ Project B       │
│ Chart Generator │                  │ Chart Generator │
│                 │                  │                 │
│ Input:          │                  │ Input:          │
│ - categories    │                  │ - categories    │
│ - values        │                  │ - values        │
│ - title         │                  │ - title         │
│                 │                  │                 │
│ Processing:     │                  │ Processing:     │
│ ❌ Fixed offset │                  │ ✅ Collision    │
│ ❌ Static font  │                  │    detection    │
│ ❌ No formatting│                  │ ✅ Adaptive font│
│                 │                  │ ✅ Smart format │
│                 │                  │ ✅ adjustText   │
│                 │                  │                 │
│ Output:         │                  │ Output:         │
│ - PNG chart     │                  │ - PNG chart     │
│   (overlaps)    │                  │   (clean)       │
│ - Test results  │                  │ - Test results  │
│ - Metrics       │                  │ - Metrics       │
└────────┬────────┘                  └────────┬────────┘
         │                                    │
         └────────────┬───────────────────────┘
                      ▼
            ┌──────────────────┐
            │ Comparison Logic │
            │                  │
            │ Compare:         │
            │ - Pass/fail      │
            │ - Metrics        │
            │ - Visual quality │
            │ - Accessibility  │
            └────────┬─────────┘
                     ▼
            ┌─────────────────┐
            │ Markdown Report │
            │                 │
            │ - Tables        │
            │ - Screenshots   │
            │ - Metrics       │
            │ - Summary       │
            └─────────────────┘
```

---

## 🎯 Test Execution Flow

```
Each Test Case (TC001-TC006)
         │
         ├─> Project A                    Project B
         │     │                             │
         │     ├─> Load test data            ├─> Load test data
         │     ├─> Generate chart            ├─> Generate chart
         │     │     │                       │     │
         │     │     ├─> Static positioning  │     ├─> Dynamic positioning
         │     │     ├─> Fixed font (12pt)   │     ├─> Adaptive font (8-14pt)
         │     │     ├─> No formatting       │     ├─> Smart formatting
         │     │     └─> Save PNG            │     └─> Save PNG
         │     │                             │
         │     ├─> Analyze chart             ├─> Analyze chart
         │     │     │                       │     │
         │     │     ├─> Detect overlaps: ✓  │     ├─> Detect overlaps: ✗
         │     │     ├─> Check readability   │     ├─> Check readability: ✓
         │     │     └─> Measure contrast    │     └─> Measure contrast: ✓
         │     │                             │
         │     ├─> Record result             ├─> Record result
         │     │     │                       │     │
         │     │     └─> Status: ❌ FAIL     │     └─> Status: ✅ PASS
         │     │                             │
         │     └─> Save to results_pre.json  └─> Save to results_post.json
         │
         └─> Compare & Report
```

---

## 📂 File Relationships

```
test_data.json
    │
    ├──> Project_A_PreFeature_UI/src/chart_generator.py (reads test data)
    │       │
    │       └──> Generates: results/charts/TC001_chart.png
    │                       results/charts/TC002_chart.png
    │                       ...
    │
    ├──> Project_A_PreFeature_UI/tests/test_pre_ui.py (reads test data)
    │       │
    │       └──> Generates: results/results_pre.json
    │                       logs/log_pre.txt
    │
    ├──> Project_B_PostFeature_UI/src/chart_generator.py (reads test data)
    │       │
    │       └──> Generates: results/charts/TC001_chart_enhanced.png
    │                       results/charts/TC002_chart_enhanced.png
    │                       ...
    │
    └──> Project_B_PostFeature_UI/tests/test_post_ui.py (reads test data)
            │
            └──> Generates: results/results_post.json
                            logs/log_post.txt

results_pre.json + results_post.json
    │
    └──> generate_comparison_report.py
            │
            └──> Generates: compare_report.md (with embedded chart paths)
```

---

## 🔍 Component Interaction

```
┌────────────────────────────────────────────────────────┐
│                    Master Runner                       │
│                   (run_all.ps1)                        │
└───────────┬────────────────────────────────────────────┘
            │
            ├──> Activate: Project A venv
            │       │
            │       ├──> Execute: pytest test_pre_ui.py
            │       │       │
            │       │       ├──> Import: chart_generator.py
            │       │       ├──> Load: test_data.json
            │       │       ├──> Run: 6 test methods
            │       │       └──> Write: results_pre.json
            │       │
            │       └──> Execute: chart_generator.py (standalone)
            │               └──> Generate: 6 chart images
            │
            ├──> Activate: Project B venv
            │       │
            │       ├──> Execute: pytest test_post_ui.py
            │       │       │
            │       │       ├──> Import: chart_generator.py
            │       │       ├──> Load: test_data.json
            │       │       ├──> Run: 6 test methods
            │       │       └──> Write: results_post.json
            │       │
            │       └──> Execute: chart_generator.py (standalone)
            │               └──> Generate: 6 enhanced chart images
            │
            └──> Execute: generate_comparison_report.py
                    │
                    ├──> Read: results_pre.json
                    ├──> Read: results_post.json
                    ├──> Compare: metrics, pass/fail, charts
                    └──> Write: compare_report.md
```

---

## 🎨 Visual Improvement Flow

```
Input Data (test_data.json)
         │
         ▼
┌─────────────────┐                    ┌─────────────────┐
│   Project A     │                    │   Project B     │
│   Rendering     │                    │   Rendering     │
└────────┬────────┘                    └────────┬────────┘
         │                                      │
         ▼                                      ▼
┌─────────────────┐                    ┌─────────────────┐
│ Chart with:     │                    │ Chart with:     │
│                 │                    │                 │
│ ❌ Overlapping  │                    │ ✅ Separated    │
│    labels       │                    │    labels       │
│                 │                    │                 │
│ ❌ Fixed font   │                    │ ✅ Adaptive     │
│    (12pt)       │                    │    font         │
│                 │                    │                 │
│ ❌ Poor         │                    │ ✅ Excellent    │
│    contrast     │                    │    contrast     │
│                 │                    │                 │
│ ❌ No number    │                    │ ✅ Formatted    │
│    formatting   │                    │    numbers      │
└────────┬────────┘                    └────────┬────────┘
         │                                      │
         ▼                                      ▼
    TC001_chart.png                    TC001_chart_enhanced.png
         │                                      │
         └──────────────┬───────────────────────┘
                        ▼
              compare_report.md
            (side-by-side comparison)
```

---

## 📊 Metrics Calculation Flow

```
Test Execution
      │
      ├──> Generate Chart
      │
      ├──> Analyze Image
      │       │
      │       ├──> Check for overlaps
      │       │     └──> Result: True/False
      │       │
      │       ├──> Measure readability
      │       │     └──> Result: Score
      │       │
      │       └──> Calculate contrast
      │             └──> Result: Ratio
      │
      ├──> Record Metrics
      │       │
      │       └──> {
      │             "accessibility_score": 7.2,
      │             "label_overlap": false,
      │             "labels_readable": true,
      │             "dynamic_positioning": true
      │           }
      │
      └──> Save to JSON
            └──> results_*.json
```

This visual flow should help users understand exactly how the project components interact and how data flows through the system!
