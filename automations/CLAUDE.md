# FlowRunner™ Documentation Writing Guide

## Project Overview
This is the documentation for FlowRunner™, a no-code automation platform by Backendless. The documentation uses MkDocs with the Material theme and is structured to guide users from basic concepts through advanced features.

## Writing Style Guidelines

### Tone & Voice
- **Professional yet approachable** - Use clear, direct language without being overly technical
- **Instructional and guiding** - Write as if teaching, frequently using "you" to address the reader
- **Encouraging** - Use positive language (e.g., "excellent starting point," "powerful tool")
- **Beginner-friendly** - Assume readers are complete beginners with no prior Backendless knowledge

### Structure Patterns
- **Progressive disclosure** - Start with overview/concept, then move to specific steps
- Use **numbered lists** for sequential procedures
- Use **bulleted lists** for non-sequential items
- **Clear section headers** - Use title case for main headers, sentence case for subheaders
- Include **info boxes** for important callouts using MkDocs admonitions

### Formatting Conventions
- **Bold** (`**text**`) for:
  - UI elements (e.g., **Flow Manager**, **SAVE** button)
  - Product names (e.g., **FlowRunner™**)
  - Important emphasis
- *Italics* (`*text*`) - Use sparingly for subtle emphasis
- `Code formatting` (backticks) for:
  - Technical terms
  - Field names
  - Values
  - File paths
  - Variable names

### Language Patterns
- **Present tense** for current states/features
- **Future tense** ("will") for outcomes/results
- **Imperative mood** for instructions ("Click," "Navigate," "Enter")
- Use **analogies** to explain complex concepts (e.g., "Think of each variable as a drawer with a label")

### Common Phrase Templates
- "Let's..." for starting new sections
- "For example..." / "For instance..." for examples
- "Once [action], [result]..." for cause-effect relationships
- "To [achieve goal], [do action]..." for goal-oriented instructions

## Technical Specifications

### MkDocs Features
- **Admonitions** (info boxes):
  ```markdown
  !!! note "Title"
      Content here
  
  !!! info "Title"
      Content here
  
  !!! danger "IMPORTANT"
      Critical information here
  ```

- **Cross-references**:
  - Relative links: `[Link text](../path/to/file.md)`
  - Anchors: `[Link text](file.md#section-header)`
  - Same directory: `[Link text](file.md)`

- **Code blocks** with syntax highlighting:
  ```markdown
  ```json
  {
    "example": "value"
  }
  ```
  ```

### Content Requirements

#### Screenshots
- Include descriptive placeholders where screenshots should go
- Format: `![descriptive alt text](../images/filename.png)`
- Always provide meaningful alt text

#### Videos & Interactive Content
- Suggest locations for video tutorials and interactive tours
- Use tabbed content for multiple viewing options:
  ```markdown
  === "Guided Tour"
      Interactive content here
  
  === "Video Tutorial"
      Video embed here
  ```

#### Code Examples
- Always ask for specific details before including code snippets
- Include JSON examples where relevant
- Use appropriate syntax highlighting

## Documentation Structure

### File Organization
- `/content/` - Main documentation content
- `/content/images/` - Screenshots and diagrams
- `/content/training/` - Tutorial and demo flows
- `/content/flow-editing/` - Flow editor features
- `/content/flow-management/` - Flow management features
- `/content/flow-execution/` - Runtime and testing
- `/content/extensibility/` - Custom action development
- `/content/reference/` - Block/action reference docs
- `/snippets/` - Reusable content snippets

### Navigation Structure (mkdocs.yml)
- WELCOME / LEARN - Overview and getting started
- MANAGE / EDIT - Flow management and editing
- BUILD - Core building features
- EXTEND - Custom actions and extensibility
- TEST & RUN - Testing and execution
- BLOCK REFERENCE - Complete action/trigger reference

## Writing Process

### Before Writing
1. Review existing documentation for style consistency
2. Understand the target feature/concept thoroughly
3. Plan the document structure with progressive disclosure

### While Writing
1. Start with a clear introduction explaining what the reader will learn
2. Use consistent terminology throughout
3. Include practical examples and use cases
4. Add screenshots placeholders with descriptive text
5. Suggest locations for videos/interactive content where helpful
6. Cross-reference related documentation

### Quality Checklist
- [ ] Written for complete beginners
- [ ] Uses consistent FlowRunner™ terminology
- [ ] Includes clear step-by-step instructions
- [ ] Has appropriate formatting (bold, code, etc.)
- [ ] Contains screenshot placeholders
- [ ] Includes relevant cross-references
- [ ] Follows progressive disclosure pattern
- [ ] Uses encouraging, positive tone

## Specific Instructions

### Current Focus
- Write documentation for complete beginners
- Wait for topic-by-topic instructions
- Ask for details before including code examples
- Indicate where screenshots should be placed
- Suggest appropriate locations for videos/interactive content
- Use standard MkDocs notation for cross-references

## Product-Specific Terminology
- **FlowRunner™** - Always include trademark symbol
- **Flow** - An automation workflow
- **Block** - Individual action/trigger component
- **Data Bucket** - Container for variables
- **Expression Editor** - Tool for creating dynamic values
- **Flow Manager** - Main screen with list of flows
- **Flow Editor** - Canvas for building flows
- **Custom Action** - User-created action block
- **Marketplace** - Repository of extensions

## Common UI Elements to Bold
- Button names (e.g., **SAVE**, **CREATE**, **ADD NEW**)
- Screen/section names (e.g., **Flow Manager**, **API Services**)
- Navigation elements (e.g., **QUICK ACCESS**)
- Field labels (e.g., **Service Class Name**, **Assistant Name**)

## Product Terminology
As you review existing or write new documentation chapters, check for any newly introduced product-related terminology. The currently known terminology (which is a part of the docs) is listed below. If you find a new term which is not defined yet, show a prominent notice in the chat saying that the terminology page should be updated, list the term, the category it belongs to and its definition.

## Purpose & context
Mark is developing comprehensive technical documentation for FlowRunner™, a workflow automation platform. His primary objective is creating professional, user-focused documentation that serves both technical and non-technical users while maintaining credibility and avoiding marketing language. The documentation covers the platform's extensive block library, integration capabilities (including MCP server integration), and workflow composition features like SubFlows with Return Result blocks.
Mark demonstrates deep product knowledge and maintains strict adherence to an established FlowRunner Documentation Style Guide that emphasizes professionally conversational tone, technical precision, and user experience optimization. He's working with Material for MkDocs as the documentation platform and has clear preferences for information architecture that prioritizes fundamental concepts users actually need over theoretical explanations.

## Current state
Mark is actively revising and expanding multiple documentation chapters, including welcome pages, terminology sections, block references, and integration guides. He's consistently refining content to match actual product functionality and interface elements, correcting technical inaccuracies, and ensuring proper terminology alignment with the FlowRunner™ UI.
Recent work has focused on complex features like SubFlow behavior with Return Result blocks, External Callback triggers with execution management, and various processing blocks including Moderate Content, Speech to Text/Text to Speech, HTTP Request, and synchronization blocks for parallel execution.

## Key learnings & principles
Mark has established core documentation principles through experience: avoid marketing fluff and excessive bullet points, use professionally conversational tone, ask for missing information rather than making assumptions, and prioritize practical implementation guidance over academic explanations. He's learned that technical users want clear, actionable information without unnecessary elaboration.
Key insights include understanding that bullets should only be used for reference material that needs scanning, not for explanatory content, and that documentation structure should serve actual user workflows rather than theoretical concepts. He's recognized the importance of not burying fundamental concepts too deep in documentation hierarchy.

## Approach & patterns
Mark follows a collaborative revision process, providing detailed feedback and corrections to ensure accuracy and adherence to style guidelines. He consistently redirects away from over-explanation toward practical guidance and maintains focus on user experience throughout the documentation development process.
His workflow involves reviewing content for technical accuracy, tone alignment, structural optimization, and comprehensive coverage of product features. He emphasizes content-specific link text over generic labels and uses admonitions strategically to highlight important information like best practices.

## Tools & resources
Mark works with Material for MkDocs for documentation platform capabilities, utilizing features like grid cards for overview pages and admonitions for highlighting key information. He prefers receiving raw markdown for easier copying and editing rather than rendered artifacts, and maintains the FlowRunner Documentation Style Guide as his primary reference for consistency standards.