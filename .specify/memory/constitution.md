<!--
Sync Impact Report:
- Version change: 1.0.0 → 1.1.0
- Modified principles: Added Article XI (Dependency Policy) - allows Rich library for UI enhancement
- Added sections: Article XI (Dependency Policy)
- Removed sections: N/A
- Templates requiring updates:
  ⚠️ plan-template.md (Update Technical Context to reflect dependency policy)
  ⚠️ spec-template.md (Update assumptions about dependencies)
  ✅ tasks-template.md (No changes required)
- Follow-up TODOs: Update plan.md for 001-calculator feature to reflect Rich dependency
- Related ADR: ADR-001 (Allow Rich Library for UI Enhancement)
-->

# Calculator Project Constitution

## Purpose

This constitution defines the mandatory principles, standards, and requirements governing the development of the Calculator project using Spec-Driven Development (SDD).

All specifications, designs, tasks, code implementations, and tests MUST comply with this constitution.

---

## Core Principles

### I. Mission

The Calculator system shall provide accurate, reliable, maintainable, and secure mathematical calculations for users.

**Primary goals** (in priority order):
1. Accuracy
2. Reliability
3. Simplicity
4. Maintainability
5. Testability

**Rationale**: Mathematical correctness is non-negotiable; all other goals support delivering correct calculations in a sustainable manner.

---

### II. Correctness First

Mathematical correctness takes precedence over development speed.

**Requirements**:
- All calculations MUST produce correct results
- Edge cases MUST be handled explicitly
- Features MUST include validation tests before deployment

**Rationale**: Calculator errors undermine user trust and can have serious consequences. Speed without correctness delivers negative value.

---

### III. Simplicity

The simplest solution that satisfies requirements MUST be preferred.

**Requirements**:
- Avoid unnecessary complexity
- Avoid premature optimization
- Avoid over-engineering
- Choose clarity over cleverness

**Rationale**: Simple code is easier to verify for correctness, maintain, and extend. Complexity is a liability that compounds over time.

---

### IV. Readability

Code MUST be understandable by new developers.

**Requirements**:
- Use meaningful, descriptive names
- Follow PEP 8 style guidelines
- Keep functions concise and focused
- Prefer clarity over cleverness

**Rationale**: Code is read far more often than written. Readability directly impacts maintainability and reduces defect rates.

---

### V. Single Responsibility

Each module, class, and function MUST have one clear responsibility.

**Separation of concerns** (MUST remain separate):
- Input handling
- Calculation logic
- Output formatting
- Error handling

**Rationale**: Single responsibility enables independent testing, reduces coupling, and makes changes safer and more predictable.

---

### VI. Maintainability

The system MUST be easy to extend without modifying existing code.

**Requirements**:
- New operations MUST require minimal modification of existing code
- Shared logic MUST NOT be duplicated
- Code MUST be modular
- Extension points MUST be clearly defined

**Rationale**: Calculator features will grow over time. Architecture must support extension without destabilizing proven functionality.

---

## Functional Requirements

### VII. Supported Operations

The calculator MUST support the following operations:

**Core Operations** (MUST be implemented):
- Addition
- Subtraction
- Multiplication
- Division

**Extended Operations** (MUST be supported):
- Power (exponentiation)
- Square Root
- Percentage
- Modulus

**Future Expansion Readiness**:

The architecture MUST allow support for the following without major redesign:
- Scientific calculations
- Trigonometric functions
- Logarithmic functions
- Memory operations

**Rationale**: Core and extended operations meet immediate user needs. Architecture must anticipate expansion to avoid costly rewrites.

---

## Quality Standards

### VIII. Reliability Standards

**Requirements**:
- Valid inputs MUST always return correct results
- Invalid inputs MUST NOT crash the application
- Error messages MUST be clear and actionable

**Error handling** (MUST be graceful):
- Division by zero
- Invalid number formats
- Unsupported operations
- Out-of-range values

**Rationale**: Reliability builds user trust. Graceful error handling prevents data loss and maintains system stability.

---

### IX. Security Standards

The calculator MUST never execute arbitrary user code.

**Forbidden practices**:
- `eval()`
- `exec()`
- Dynamic code execution from user input

**Requirements**:
- Validate all user input before processing
- Sanitize external input
- Reject malformed expressions safely
- Use explicit parsing, never code evaluation

**Rationale**: Code execution vulnerabilities are critical security risks. Calculators are common attack vectors due to expression parsing.

---

### X. Testing Standards

Every feature MUST include tests before being marked complete.

**Minimum coverage requirements**:
- Normal cases (happy path)
- Edge cases (boundaries)
- Error cases (invalid input)

**Example test coverage**:
- `2 + 3 = 5` (normal)
- `10 / 2 = 5` (normal)
- `10 / 0 → Error` (error)
- `sqrt(0) = 0` (edge)
- `sqrt(-1) → Error` (error)

**Coverage target**: 90% or greater code coverage

**Rationale**: Untested code is untrustworthy code. Mathematical operations demand comprehensive test coverage to ensure correctness.

---

### XI. Dependency Policy

The calculator MUST maintain a minimal dependency footprint while allowing selective dependencies that provide significant value.

**Core Principle**: Business logic MUST remain dependency-free. UI enhancements MAY use approved external libraries.

**Dependency Categories**:

1. **Business Logic Dependencies** (FORBIDDEN):
   - Mathematical operations MUST use Python standard library only
   - Validation logic MUST use Python standard library only
   - Core calculator logic MUST NOT depend on external packages

2. **UI Enhancement Dependencies** (SELECTIVELY ALLOWED):
   - Terminal formatting and presentation MAY use approved libraries
   - Each UI dependency REQUIRES an ADR justifying its inclusion
   - UI dependencies MUST NOT affect core calculation correctness

3. **Development Dependencies** (ALLOWED):
   - Testing frameworks (pytest, pytest-cov)
   - Code quality tools (linters, formatters)
   - Documentation generators

**Approved Dependencies**:
- **Rich** (v13.x): Terminal UI enhancement - formatting, colors, tables, panels
  - Justification: See ADR-001
  - Scope: Presentation layer only
  - Status: Approved 2026-06-12

**Approval Criteria for New Dependencies**:
A new runtime dependency may be approved ONLY if:
1. It provides significant user value (not developer convenience)
2. It is well-maintained (active development, responsive maintainers)
3. It has proven stability (mature API, large user base)
4. It is scoped to presentation/interaction layer (not business logic)
5. It has minimal transitive dependencies
6. An ADR documents the decision

**Rationale**: Zero dependencies was the initial goal to maximize simplicity and deployment ease. However, modern CLI users expect rich terminal interfaces with colors and formatting. By restricting dependencies to the presentation layer only and requiring ADRs, we maintain architectural integrity while improving user experience. Business logic remains pure, testable, and portable.

---

## Code Quality Standards

### XI. Code Style and Structure

**Requirements**:
- Follow PEP 8 style guidelines
- Use type hints where practical
- Keep functions focused and concise
- Avoid duplicated code (DRY principle)

**Naming standards**:

✅ **Good**:
- `add_numbers()`
- `divide_numbers()`
- `calculate_result()`

❌ **Bad**:
- `x()`
- `abc()`
- `doStuff()`

**Rationale**: Consistent style reduces cognitive load. Good names make code self-documenting and reduce the need for comments.

---

### XII. Documentation Standards

Every public function MUST contain documentation specifying:
- Purpose (what it does)
- Parameters (inputs and types)
- Return value (output and type)
- Possible exceptions (error conditions)

**Additional requirements**:
- Major features MUST be documented in user-facing docs
- README MUST remain updated with current capabilities
- Breaking changes MUST be documented in CHANGELOG

**Rationale**: Documentation enables effective use and maintenance. Undocumented code becomes technical debt rapidly.

---

### XIII. Project Structure

**Recommended structure**:

```
calculator/
├── calculator.py        # Main entry point
├── operations.py        # Mathematical operations
├── validators.py        # Input validation
├── tests/
│   ├── test_operations.py
│   └── test_validators.py
├── requirements.txt     # Dependencies
├── README.md           # User documentation
└── CONSTITUTION.md     # This file
```

**Rationale**: Clear structure enables quick navigation and sets expectations for where new code belongs.

---

### XIV. Definition of Done

A feature is considered complete ONLY when ALL criteria are met:

1. ✅ Specification exists
2. ✅ Design is approved
3. ✅ Code is implemented
4. ✅ Tests are written
5. ✅ Tests pass
6. ✅ Documentation is updated
7. ✅ No critical defects remain

**Rationale**: "Done" must have a clear, verifiable definition to prevent accumulation of incomplete work.

---

## Governance

### Amendment Process

This constitution may be amended ONLY when a proposed change:

1. Improves maintainability, OR
2. Improves reliability, OR
3. Improves security, OR
4. Improves developer productivity,

**AND** does NOT compromise correctness.

**Amendment procedure**:
- Document the proposed change and rationale
- Create an ADR (Architecture Decision Record) via `/sp.adr`
- Obtain approval from project maintainers
- Update constitution version according to semantic versioning
- Update all dependent artifacts (specs, plans, tasks)

### Compliance

- All PRs and code reviews MUST verify compliance with this constitution
- Complexity MUST be justified against constitutional principles
- Constitutional violations require explicit documentation and approval
- This constitution supersedes all other development practices

### Priority Hierarchy

The project MUST prioritize in this order:

**Correctness > Reliability > Maintainability > Performance > Convenience**

No implementation decision may violate this priority order.

---

**Version**: 1.1.0 | **Ratified**: 2026-06-10 | **Last Amended**: 2026-06-12

**Amendment History**:
- **1.1.0** (2026-06-12): Added Article XI (Dependency Policy) - allows Rich library for UI enhancement per ADR-001
- **1.0.0** (2026-06-10): Initial constitution ratified
