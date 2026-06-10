# Tasks: Calculator

**Input**: Design documents from `/specs/001-calculator/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are OPTIONAL in this task list. Since the specification emphasizes TDD and constitutional requirements mandate 90% coverage, tests are included following red-green-refactor workflow.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project structure per plan.md

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project directory structure (src/, tests/unit/, tests/integration/)
- [x] T002 Initialize Python 3.8+ virtual environment and verify installation
- [x] T003 [P] Create requirements.txt with pytest>=7.0.0 and pytest-cov>=4.0.0
- [x] T004 [P] Create .gitignore for Python projects (venv/, __pycache__/, *.pyc, .pytest_cache/, .coverage)
- [x] T005 [P] Create empty module files: src/__init__.py, tests/__init__.py, tests/unit/__init__.py, tests/integration/__init__.py

**Checkpoint**: Foundation structure ready - user story implementation can begin

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T006 Create src/operations.py stub with module docstring and imports
- [x] T007 Create src/validators.py stub with module docstring and imports
- [x] T008 Create src/calculator.py stub with module docstring, imports, and if __name__ == "__main__" block

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Core Arithmetic Operations (Priority: P1) 🎯 MVP

**Goal**: Implement and verify add, subtract, multiply, and divide operations with correct mathematical results

**Independent Test**: Run calculator, select operation 1-4, enter two valid numbers, verify correct result displayed

### Tests for User Story 1 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation (Red-Green-Refactor)**

- [x] T009 [P] [US1] Create test file tests/unit/test_operations.py with imports and test class
- [x] T010 [P] [US1] Write test_add_positive_numbers, test_add_negative_numbers, test_add_zero in tests/unit/test_operations.py
- [x] T011 [P] [US1] Write test_subtract_positive, test_subtract_negative, test_subtract_result_negative in tests/unit/test_operations.py
- [x] T012 [P] [US1] Write test_multiply_positive, test_multiply_negative, test_multiply_by_zero in tests/unit/test_operations.py
- [x] T013 [P] [US1] Write test_divide_positive, test_divide_result_decimal, test_divide_by_zero_raises_error in tests/unit/test_operations.py

### Implementation for User Story 1

- [x] T014 [P] [US1] Implement add(a: float, b: float) -> float in src/operations.py with docstring and type hints
- [x] T015 [P] [US1] Implement subtract(a: float, b: float) -> float in src/operations.py with docstring and type hints
- [x] T016 [P] [US1] Implement multiply(a: float, b: float) -> float in src/operations.py with docstring and type hints
- [x] T017 [US1] Implement divide(a: float, b: float) -> float in src/operations.py with division-by-zero check raising ValueError
- [x] T018 [US1] Run pytest tests/unit/test_operations.py and verify all US1 tests pass

**Checkpoint**: At this point, User Story 1 core arithmetic operations are fully functional and testable independently

---

## Phase 4: User Story 2 - Input Validation and Error Handling (Priority: P1)

**Goal**: Validate user input and handle errors gracefully without crashes

**Independent Test**: Enter invalid inputs (letters, empty, division by zero) and verify appropriate error messages with continued operation

### Tests for User Story 2 ⚠️

- [x] T019 [P] [US2] Create test file tests/unit/test_validators.py with imports and test class
- [x] T020 [P] [US2] Write test_validate_numeric_input_valid_integer, test_valid_decimal, test_valid_negative in tests/unit/test_validators.py
- [x] T021 [P] [US2] Write test_validate_numeric_input_invalid_letters, test_invalid_empty, test_invalid_special_chars in tests/unit/test_validators.py
- [x] T022 [P] [US2] Write test_validate_menu_choice_valid_range, test_invalid_out_of_range, test_invalid_non_numeric in tests/unit/test_validators.py
- [x] T023 [P] [US2] Write test_validate_non_negative_valid, test_negative_rejected in tests/unit/test_validators.py

### Implementation for User Story 2

- [x] T024 [P] [US2] Implement validate_numeric_input(user_input: str) -> Tuple[bool, str] in src/validators.py
- [x] T025 [P] [US2] Implement validate_menu_choice(user_input: str) -> Tuple[bool, str] in src/validators.py
- [x] T026 [P] [US2] Implement validate_non_negative(number: float) -> Tuple[bool, str] in src/validators.py
- [x] T027 [US2] Add error message constants at top of src/validators.py (ERROR_INVALID_NUMBER, ERROR_EMPTY_INPUT, ERROR_INVALID_MENU, etc.)
- [x] T028 [US2] Run pytest tests/unit/test_validators.py and verify all US2 tests pass

**Checkpoint**: At this point, User Stories 1 AND 2 both work - calculator has operations and validation

---

## Phase 5: User Story 3 - Extended Mathematical Operations (Priority: P2)

**Goal**: Implement power, square root, percentage, and modulus operations

**Independent Test**: Run calculator, select operations 5-8, verify correct results for power, sqrt, percentage, modulus

### Tests for User Story 3 ⚠️

- [x] T029 [P] [US3] Write test_power_positive_exponent, test_power_zero_exponent, test_power_negative_exponent in tests/unit/test_operations.py
- [x] T030 [P] [US3] Write test_square_root_positive, test_square_root_zero, test_square_root_negative_raises_error in tests/unit/test_operations.py
- [x] T031 [P] [US3] Write test_percentage_basic, test_percentage_zero in tests/unit/test_operations.py
- [x] T032 [P] [US3] Write test_modulus_basic, test_modulus_zero_divisor_raises_error in tests/unit/test_operations.py

### Implementation for User Story 3

- [x] T033 [P] [US3] Implement power(base: float, exponent: float) -> float in src/operations.py using math.pow
- [x] T034 [P] [US3] Implement square_root(number: float) -> float in src/operations.py with negative check raising ValueError
- [x] T035 [P] [US3] Implement percentage(percent: float, of_value: float) -> float in src/operations.py
- [x] T036 [P] [US3] Implement modulus(a: float, b: float) -> float in src/operations.py with zero divisor check
- [x] T037 [US3] Run pytest tests/unit/test_operations.py and verify all US3 tests pass

**Checkpoint**: All mathematical operations (core + extended) are now implemented and tested

---

## Phase 6: User Story 4 - Session Management (Priority: P2)

**Goal**: Provide menu-based interface, handle multiple calculations per session, allow clean exit

**Independent Test**: Launch calculator, perform 3+ different calculations, exit cleanly via menu option

### Tests for User Story 4 ⚠️

- [ ] T038 [US4] Create test file tests/integration/test_calculator.py with imports for integration testing
- [ ] T039 [US4] Write integration test for complete calculation workflow (menu → input → operation → result → menu) in tests/integration/test_calculator.py
- [ ] T040 [US4] Write integration test for multiple consecutive calculations in tests/integration/test_calculator.py
- [ ] T041 [US4] Write integration test for clean exit via menu option in tests/integration/test_calculator.py

### Implementation for User Story 4

- [ ] T042 [US4] Implement display_menu() -> None in src/calculator.py that prints menu with options 1-8 and 0 for exit
- [ ] T043 [US4] Implement get_menu_choice() -> int in src/calculator.py using validate_menu_choice from validators
- [ ] T044 [US4] Implement get_numeric_input(prompt: str) -> float in src/calculator.py with validation loop
- [ ] T045 [US4] Implement execute_operation(choice: int) -> None in src/calculator.py with if/elif dispatch to operations
- [ ] T046 [US4] Implement main_loop() -> None in src/calculator.py with while True loop, menu display, choice handling
- [ ] T047 [US4] Implement main() -> None in src/calculator.py with welcome message, main_loop call, KeyboardInterrupt handler
- [ ] T048 [US4] Update if __name__ == "__main__" block in src/calculator.py to call main()
- [ ] T049 [US4] Run pytest tests/integration/test_calculator.py and verify all US4 integration tests pass

**Checkpoint**: All user stories are now independently functional - complete calculator application

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories and final quality checks

- [ ] T050 [P] Create README.md with installation instructions, usage examples, and feature list
- [ ] T051 [P] Add comprehensive docstrings to all functions in src/operations.py following Google style
- [ ] T052 [P] Add comprehensive docstrings to all functions in src/validators.py following Google style
- [ ] T053 [P] Add comprehensive docstrings to all functions in src/calculator.py following Google style
- [ ] T054 Run pytest --cov=src --cov-report=term-missing and verify >90% coverage
- [ ] T055 Run full test suite with pytest -v and verify all tests pass
- [ ] T056 Manual integration test following specs/001-calculator/quickstart.md validation scenarios
- [ ] T057 Code review against .specify/memory/constitution.md principles (PEP 8, naming, simplicity, security)
- [ ] T058 Verify all 18 functional requirements from spec.md are implemented
- [ ] T059 Final smoke test: perform all 8 operations successfully in one session

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-6)**: All depend on Foundational phase completion
  - User Story 1 (P1): Can start after Foundational - No dependencies on other stories
  - User Story 2 (P1): Can start after Foundational - Enhances US1 but independently testable
  - User Story 3 (P2): Can start after Foundational - No dependencies on US1/US2
  - User Story 4 (P2): Should start after US1+US2 complete (needs operations and validation to be useful)
- **Polish (Phase 7)**: Depends on all user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Independent - implements core operations only
- **User Story 2 (P1)**: Independent - implements validation layer only
- **User Story 3 (P2)**: Independent - adds extended operations
- **User Story 4 (P2)**: Weak dependency on US1+US2 (needs something to orchestrate, but can implement menu structure independently)

### Within Each User Story

- Tests MUST be written and FAIL before implementation (Red-Green-Refactor)
- Within implementation: parallelizable tasks marked [P] can run simultaneously
- Story complete only when all its tests pass

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel (T003, T004, T005)
- All test-writing tasks within a user story marked [P] can run in parallel
- All operation implementation tasks marked [P] can run in parallel (different functions)
- Different user stories can be worked on in parallel by different team members after Foundational completes

---

## Parallel Example: User Story 1

```bash
# After Foundational phase completes, launch all US1 tests in parallel:
Task T010: "Write test_add_* tests"
Task T011: "Write test_subtract_* tests"
Task T012: "Write test_multiply_* tests"
Task T013: "Write test_divide_* tests"

# Then launch all US1 implementations in parallel:
Task T014: "Implement add()"
Task T015: "Implement subtract()"
Task T016: "Implement multiply()"
Task T017: "Implement divide()"
```

---

## Implementation Strategy

### MVP First (User Story 1 + User Story 2 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (Core Arithmetic)
4. Complete Phase 4: User Story 2 (Validation & Error Handling)
5. **STOP and VALIDATE**: Calculator now has 4 operations with validation - this is MVP
6. Can demo/deploy basic calculator before continuing

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Partial calculator (operations work with manual valid input)
3. Add User Story 2 → Test independently → Robust calculator (operations + validation)
4. Add User Story 3 → Test independently → Extended calculator (8 operations total)
5. Add User Story 4 → Test independently → Complete calculator (full session management)
6. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1 (Core Operations)
   - Developer B: User Story 2 (Validation)
   - Developer C: User Story 3 (Extended Operations)
   - Developer D: User Story 4 (Session Management - waits for US1+US2)
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies on incomplete tasks
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Follow Red-Green-Refactor: write failing tests first, then implement to make them pass
- Commit after each task or logical group of related tasks
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
- Target: 90%+ test coverage per constitutional requirement
