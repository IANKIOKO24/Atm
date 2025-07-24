# Medical Dashboard

A modern, responsive medical dashboard built using the design system extracted from the original design screenshot. This implementation replicates the exact visual design, color palette, typography, and layout structure in a web-based interface.

## 🎨 Design System

This dashboard implements a comprehensive design system based on the JSON profile extracted from the original design:

### Color Palette
- **Primary Background**: `#1a1b2e`
- **Surface**: `#16213e` 
- **Card Background**: `#0f1829`
- **Accent Colors**: Teal (`#00d4aa`), Green (`#4caf50`), Yellow (`#ffc107`), Purple (`#9c27b0`), Blue (`#2196f3`)

### Typography
- **Font Family**: Segoe UI, Arial, sans-serif
- **Sizes**: H1 (24px), H2 (20px), H3 (16px), Body (14px), Caption (12px)
- **Colors**: Primary (`#ffffff`), Secondary (`#b0bec5`), Muted (`#78909c`)

### Components
- **Calendar Widget**: Interactive calendar with current day highlighting
- **Bar Charts**: Animated charts using Chart.js with custom dark theme
- **Stat Cards**: Gradient background cards with icons and metrics
- **Data Table**: Responsive table with hover effects and status badges

## 🚀 Quick Start

### Option 1: Web Version (Recommended)
```bash
# Start the development server
python3 server.py

# Open http://localhost:8000 in your browser
```

### Option 2: Tkinter Version (Requires Dependencies)
```bash
# Install dependencies
pip install matplotlib numpy

# Run the application
python3 medical_dashboard.py
```

## 📁 Project Structure

```
medical-dashboard/
├── design_profile.json     # Complete design system specification
├── index.html             # Main dashboard HTML structure
├── styles.css             # CSS implementing the design system
├── script.js              # JavaScript for interactivity and charts
├── server.py              # Development server
├── medical_dashboard.py   # Tkinter implementation
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🎯 Features

### Interactive Components
- **✅ Calendar**: Click to select dates, current day highlighting
- **📊 Charts**: Animated bar charts with hover tooltips
- **📋 Data Table**: Sortable appointments with status badges
- **🎛️ Stat Cards**: Hover effects and gradient backgrounds
- **📱 Responsive**: Adapts to different screen sizes

### Design Fidelity
- **🎨 Exact Color Matching**: All colors match the original design
- **📐 Consistent Spacing**: Uses the design system spacing scale
- **🖼️ Component Structure**: Maintains the original layout grid
- **✨ Animations**: Smooth transitions and hover effects

## 🛠️ Implementation Details

### Design System Usage
The entire interface is built using CSS custom properties (variables) that map directly to the JSON design profile:

```css
:root {
    --primary-background: #1a1b2e;
    --primary-surface: #16213e;
    --accent-teal: #00d4aa;
    --font-size-h1: 24px;
    --spacing-md: 16px;
    --border-radius-large: 12px;
}
```

### Component Architecture
Each component follows the design system specifications:

1. **Calendar Widget**: Grid-based layout with interactive day selection
2. **Chart Components**: Chart.js integration with dark theme configuration
3. **Stat Cards**: CSS gradients matching the design with proper icon placement
4. **Data Table**: Custom styling for dark theme with status badge system

### Responsive Behavior
- **Desktop**: 3-column layout (calendar + 2 charts)
- **Tablet**: Stacked layout with 2-column stat cards
- **Mobile**: Single column with full-width components

## 🎛️ Customization

### Updating Colors
Modify the CSS custom properties in `styles.css`:

```css
:root {
    --primary-background: #your-color;
    --accent-teal: #your-accent;
}
```

### Adding Data
Update the JavaScript data arrays in `script.js`:

```javascript
// Chart data
data: [250, 180, 320, 380, 290, 420, 350]

// Table data
const appointmentsData = [
    ['1', '102-23-243', 'Ronald Richards', 'Routine Checkup']
];
```

### Extending Components
The design system supports easy component extension:

1. Use existing CSS classes and variables
2. Follow the established spacing and color patterns
3. Maintain the component structure from the JSON profile

## 🔧 Development

### Adding New Features
1. **New Stat Cards**: Add to the stat cards grid in HTML
2. **Chart Types**: Extend Chart.js configurations in JavaScript
3. **Table Columns**: Update table structure and corresponding CSS
4. **Interactive Elements**: Use existing hover and click patterns

### Performance Considerations
- **Charts**: Chart.js is loaded from CDN for optimal performance
- **Animations**: CSS transitions are hardware-accelerated
- **Images**: Icons use Unicode emojis for fast loading
- **Responsive**: CSS Grid and Flexbox for efficient layouts

## 📊 Design System Reference

The complete design system is documented in `design_profile.json`, including:

- **Color Palette**: All colors with hex values
- **Typography**: Font sizes, weights, and hierarchy
- **Spacing**: Consistent spacing scale
- **Components**: Detailed specifications for each component
- **Layout**: Grid structure and responsive behavior
- **Tkinter Guide**: Implementation guide for desktop applications

## 🌐 Browser Support

- **Modern Browsers**: Chrome, Firefox, Safari, Edge (latest versions)
- **CSS Grid**: Required for layout
- **Chart.js**: Supports all major browsers
- **ES6**: Modern JavaScript features used

## 📱 Mobile Experience

The dashboard is fully responsive with:
- **Touch-friendly**: Large touch targets for mobile interaction
- **Optimized Layout**: Single-column stacking on small screens
- **Performance**: Optimized for mobile rendering
- **Accessibility**: Proper contrast ratios and focus indicators

---

**Built with**: HTML5, CSS3, JavaScript ES6, Chart.js  
**Design System**: Extracted from original medical dashboard screenshot  
**Implementation**: Web-first with Tkinter fallback