---
allowed-tools: Bash(dotnet build:*), Bash(dotnet:*), Bash(find:*), Bash(grep:*), Read, Edit, Write, Glob
argument-hint: [assembly-name-or-alias-or-path]
description: Compile Unity C# assembly with intelligent name matching and auto-fix errors
---

# Unity Assembly Compiler

You are to compile the specified Unity C# assembly using `dotnet build` and automatically fix any compilation errors that occur.

## Parameters
- `$1`: The name, alias, partial name, or **direct path** of the Unity assembly/project to compile
  - **Path mode**: If `$1` is a valid .csproj file path (relative or absolute), use it directly
  - **Name mode**: If `$1` is a name/alias, use intelligent matching to find the project
- `$ARGUMENTS`: All arguments passed to the command

## Your Task

**CRITICAL**: First determine if input is a path or name (see "Input Analysis" section below)

Then execute the compilation workflow:
1. **Smart Assembly Discovery**: Use intelligent matching to find the correct project file (or use direct path)
2. **Execute compilation**: Run `dotnet build` on the target project
3. **Analyze errors**: Parse compilation errors and categorize them
4. **Apply fixes**: Automatically fix common compilation errors
5. **Rebuild**: Run compilation again to verify fixes
6. **Report**: Summarize what was fixed

## Smart Assembly Name Matching

### Common Unity Assembly Aliases
- **main/primary/game/runtime** → `Assembly-CSharp`
- **editor/edit/editor-scripts** → `Assembly-CSharp-Editor`
- **firstpass/preimport/pre-import** → `Assembly-CSharp-firstpass`
- **editor-firstpass/editor-preimport** → `Assembly-CSharp-Editor-firstpass`

### Assembly Discovery Process
1. **Path Detection**: If `$1` is a valid .csproj file path, use it directly (highest priority)
2. **Direct Match**: Try exact match with assembly name
3. **Alias Resolution**: Map common aliases to actual assembly names
4. **Fuzzy Matching**: Search for partial matches in available projects
5. **Unity Standards**: Check for standard Unity assembly naming patterns


## Error Analysis and Fix Strategy

If the build fails, analyze the errors and apply these fixes systematically:

### CS0103: Name does not exist in current context
- Add missing `using` statements at the top of the file
- Common Unity namespaces: `UnityEngine`, `UnityEngine.UI`, `System.Collections.Generic`, `System.Linq`

### CS0246: Type or namespace name could not be found
- Add appropriate using directives
- Check for typos in type names
- Add missing assembly references if needed

### CS0117: Member does not exist
- Fix property/method name typos
- Check Unity API changes and deprecations
- Use correct Unity API methods

### CS1061: Extension method not found
- Add `using System.Linq;` for LINQ methods
- Check for correct method signatures

### CS0029: Cannot implicitly convert type
- Add explicit type casting
- Fix variable type declarations
- Use correct Unity component types

### CS1503: Argument mismatch
- Fix method parameter types
- Add missing arguments
- Correct parameter order

## Execution Workflow

### Step 0: Input Type Detection (MUST DO FIRST)
**Immediately check** if `$1` is a valid file path:
```bash
test -f "$1" && echo "PATH_MODE" || echo "NAME_MODE"
```
- If `PATH_MODE` and ends with `.csproj`: Set `TARGET_PROJECT="$1"`
- If `NAME_MODE`: Use assembly discovery to find matching `.csproj` file

### Step 1: Initial Compilation
Run `dotnet build <TARGET_PROJECT> --verbosity normal` and capture output.

### Step 2: Error Analysis
If build fails, parse output to extract:
- Error codes (CSxxxx)
- File paths and line numbers
- Error descriptions

### Step 3: Apply Fixes
For each error:
1. Read the problematic file
2. Apply fix based on error type (see "Error Analysis and Fix Strategy")
3. Save changes

### Step 4: Verification
Re-run compilation to confirm:
- Errors resolved
- No new errors introduced

### Step 5: Report Results
Summary including:
- Initial error count
- Fixes applied
- Final build status

## Context: Available Projects in Workspace

All C# projects available for name matching:
!`find . -name "*.csproj" -type f | head -20`

Use this list only if NAME_MODE is triggered (i.e., `$1` is not a valid file path).

## Best Match Analysis:
The best matching assembly is determined by:
1. **Path validation** (if `$1` is a valid .csproj file path)
2. Exact name matches to `$1`
3. Common Unity assembly aliases
4. Fuzzy string matching
5. Unity naming conventions

## Safety Measures
- Always create backups before modifying files
- Use conservative fix approaches
- Validate changes don't break existing functionality
- Provide clear explanations of all modifications

Execute the compilation and fix process now using the best-matching assembly.