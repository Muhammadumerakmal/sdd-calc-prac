# ADR-001: Allow Rich Library for Terminal UI Enhancement

> **Scope**: Amend dependency policy to allow Rich library for improved user interface while maintaining minimal dependency philosophy.

- **Status:** Proposed
- **Date:** 2026-06-12
- **Feature:** 001-calculator
- **Context:** Calculator UI Enhancement

<!-- Significance checklist (ALL must be true to justify this ADR)
     ✅ 1) Impact: Changes constitutional dependency policy, sets precedent for future UI libraries
     ✅ 2) Alternatives: Multiple viable options (standard lib, colorama, curses, Rich, Textual)
     ✅ 3) Scope: Cross-cutting - affects entire UI layer and constitutional principles
-->

## Decision

**Amend the Calculator constitution to allow the Rich library as an approved dependency for terminal UI enhancement.**

Specifically:
- **Add Rich** (v13.x) as the first approved external runtime dependency
- **Preserve principle**: Maintain "minimal dependencies" philosophy - only add dependencies that provide significant UX value
- **Scope limitation**: Rich is approved for presentation layer only (not for core calculation logic)
- **Constitutional amendment**: Update Article III (Simplicity) to distinguish between "business logic dependencies" (still zero) and "UI enhancement dependencies" (selectively allowed)

## Consequences

### Positive

- **Significantly improved UX**: Colors, formatted tables, progress indicators, better readability
- **Professional appearance**: Modern terminal UI that matches user expectations for CLI tools in 2026
- **Better error presentation**: Rich can display errors with context, syntax highlighting, and visual hierarchy
- **Accessibility**: Rich handles terminal detection and gracefully degrades on non-color terminals
- **Maintainability**: Rich is actively maintained, well-documented, widely adopted (45M+ downloads/month)
- **Development velocity**: Rich provides high-level primitives that would take significant effort to build from scratch

### Negative

- **External dependency**: Users must `pip install rich` (adds ~500KB to install size)
- **Breaking constitutional principle**: Violates current "zero external dependencies" constraint
- **Update risk**: Future Rich API changes could require code updates
- **Startup time**: Minimal overhead (~50ms) for importing Rich on first run
- **Complexity**: Adds one more component to understand and maintain
- **Deployment consideration**: Requires updating requirements.txt and installation documentation

## Alternatives Considered

### Alternative A: Standard Library Only (Current State)
- **Pros**: Zero dependencies, simplest deployment, fastest startup
- **Cons**: Plain text output only, no colors, limited formatting, dated appearance
- **Why rejected**: UX is significantly inferior; users expect modern CLI tools to have colored output

### Alternative B: Colorama
- **Pros**: Lighter than Rich (~50KB), cross-platform color support, simpler API
- **Cons**: Only provides colors, no tables/progress bars/layouts, still requires external dependency
- **Why rejected**: If we're adding a dependency, Rich provides far more value for similar cost

### Alternative C: Curses (Standard Library)
- **Pros**: Part of standard library (no new dependency), full TUI capability
- **Cons**: Complex API, poor Windows support, overkill for simple output formatting
- **Why rejected**: Complexity doesn't justify the "no dependency" benefit; harder to maintain

### Alternative D: Textual (Rich's full TUI framework)
- **Pros**: Most powerful, reactive UI, widgets, layouts
- **Cons**: Much heavier dependency, overkill for calculator, steeper learning curve
- **Why rejected**: Over-engineered for our use case; Rich provides the right balance

### Alternative E: Build custom formatting library
- **Pros**: Zero external dependencies, full control
- **Cons**: Significant development effort (weeks), testing burden, maintenance cost, likely inferior to Rich
- **Why rejected**: Not economically justified; violates "simplicity" principle by reinventing the wheel

## Rationale for Selection

Rich provides the **optimal balance** between:
- **Value**: Dramatic UX improvement with minimal code changes
- **Cost**: Single well-maintained dependency with stable API
- **Simplicity**: High-level API is simpler than low-level formatting code
- **Philosophy**: Aligns with "simplicity" and "user value first" - we're not adding complexity, we're adding capability

**Constitutional Alignment**: While this technically violates the letter of "zero dependencies," it upholds the *spirit* of the constitution:
- **Article I (Mission)**: Improves reliability and maintainability through better error presentation
- **Article III (Simplicity)**: Rich's high-level API is *simpler* than manual ANSI code formatting
- **Article IV (Readability)**: Rich makes output more readable for users

## Implementation Impact

**Files to Update:**
1. `.specify/memory/constitution.md` - Amend Article III and VII
2. `requirements.txt` - Add `rich>=13.0.0`
3. `specs/001-calculator/plan.md` - Update Technical Context section
4. `src/calculator.py` - Integrate Rich Console, Panel, Table components
5. `README.md` - Update installation instructions

**Migration Strategy:**
- Phase 1: Constitutional amendment (this ADR)
- Phase 2: Update planning documents
- Phase 3: Add Rich to requirements and verify installation
- Phase 4: Incremental Rich integration (menu → results → errors)
- Phase 5: Update tests to handle Rich formatting
- Phase 6: Update documentation

## References

- Feature Spec: `specs/001-calculator/spec.md`
- Implementation Plan: `specs/001-calculator/plan.md`
- Related ADRs: None (first ADR)
- Rich Documentation: https://rich.readthedocs.io/
- Rich GitHub: https://github.com/Textualize/rich (19k+ stars, proven stability)
- Evaluator Evidence: User explicitly requested Rich integration for UX improvement
