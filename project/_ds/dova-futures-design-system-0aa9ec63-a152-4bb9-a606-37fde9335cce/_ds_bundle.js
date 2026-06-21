/* @ds-bundle: {"format":3,"namespace":"DOVAFuturesDesignSystem_0aa9ec","components":[{"name":"Badge","sourcePath":"components/core/Badge.jsx"},{"name":"Button","sourcePath":"components/core/Button.jsx"},{"name":"Eyebrow","sourcePath":"components/core/Eyebrow.jsx"},{"name":"SectionHeader","sourcePath":"components/core/SectionHeader.jsx"},{"name":"Stat","sourcePath":"components/core/Stat.jsx"},{"name":"Tag","sourcePath":"components/core/Tag.jsx"},{"name":"Field","sourcePath":"components/forms/Field.jsx"},{"name":"Input","sourcePath":"components/forms/Input.jsx"},{"name":"Textarea","sourcePath":"components/forms/Textarea.jsx"},{"name":"Card","sourcePath":"components/surfaces/Card.jsx"},{"name":"ServiceCard","sourcePath":"components/surfaces/Card.jsx"},{"name":"ProjectCard","sourcePath":"components/surfaces/Card.jsx"}],"sourceHashes":{"components/core/Badge.jsx":"a6491acc5c9f","components/core/Button.jsx":"c5d4dde5862a","components/core/Eyebrow.jsx":"9b063acbba95","components/core/SectionHeader.jsx":"b355a735cab0","components/core/Stat.jsx":"3b2c5fb8dc27","components/core/Tag.jsx":"4a40c0614f53","components/forms/Field.jsx":"5fe4baca9398","components/forms/Input.jsx":"e55857ded955","components/forms/Textarea.jsx":"c1e42406dadb","components/surfaces/Card.jsx":"5f5dc6838477","ui_kits/dova-website/pages.jsx":"cdf760b39a48","ui_kits/dova-website/screens.jsx":"1aedf9e7e447"},"inlinedExternals":[],"unexposedExports":[]} */

(() => {

const __ds_ns = (window.DOVAFuturesDesignSystem_0aa9ec = window.DOVAFuturesDesignSystem_0aa9ec || {});

const __ds_scope = {};

(__ds_ns.__errors = __ds_ns.__errors || []);

// components/core/Badge.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * DOVA Futures — Badge / Tag
 * Small status or category label. `solid` for status, `soft` tint, `outline` pill
 * for skill/category chips (portfolio style).
 */
function Badge({
  children,
  variant = "soft",
  tone = "green",
  style = {},
  ...rest
}) {
  const palettes = {
    green: {
      solid: "var(--green-700)",
      soft: "var(--green-100)",
      softText: "var(--green-700)",
      line: "var(--green-500)"
    },
    clay: {
      solid: "var(--clay)",
      soft: "var(--clay-100)",
      softText: "var(--clay-dark)",
      line: "var(--clay)"
    },
    neutral: {
      solid: "var(--ink-800)",
      soft: "var(--sand)",
      softText: "var(--ink-800)",
      line: "var(--stone)"
    },
    success: {
      solid: "var(--success)",
      soft: "#DCEBE2",
      softText: "#1C4636",
      line: "var(--success)"
    },
    warning: {
      solid: "var(--warning)",
      soft: "#F5E6C8",
      softText: "#7A5310",
      line: "var(--warning)"
    },
    danger: {
      solid: "var(--danger)",
      soft: "#F1D9D6",
      softText: "#7A241B",
      line: "var(--danger)"
    }
  };
  const p = palettes[tone];
  const variants = {
    solid: {
      background: p.solid,
      color: "var(--cream)",
      border: "1px solid transparent"
    },
    soft: {
      background: p.soft,
      color: p.softText,
      border: "1px solid transparent"
    },
    outline: {
      background: "transparent",
      color: p.softText,
      border: `1px solid ${p.line}`
    }
  };
  const isPill = variant === "outline";
  return /*#__PURE__*/React.createElement("span", _extends({
    style: {
      display: "inline-flex",
      alignItems: "center",
      gap: "6px",
      fontFamily: "var(--font-body)",
      fontSize: "12px",
      fontWeight: 600,
      letterSpacing: isPill ? "0.04em" : "0.02em",
      textTransform: isPill ? "uppercase" : "none",
      padding: isPill ? "6px 14px" : "4px 10px",
      borderRadius: isPill ? "var(--radius-pill)" : "var(--radius-sm)",
      lineHeight: 1.2,
      ...variants[variant],
      ...style
    }
  }, rest), children);
}
Object.assign(__ds_scope, { Badge });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Badge.jsx", error: String((e && e.message) || e) }); }

// components/core/Button.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * DOVA Futures — Button
 * Premium architectural button. `primary` = forest-green fill with green-tinted
 * shadow + lift. `cream` / `outlineLight` are for dark-green sections; outlines
 * invert on hover.
 */
function Button({
  children,
  variant = "primary",
  size = "md",
  as = "button",
  iconLeft = null,
  iconRight = null,
  full = false,
  disabled = false,
  style = {},
  ...rest
}) {
  const [hover, setHover] = React.useState(false);
  const sizes = {
    sm: {
      padding: "9px 18px",
      fontSize: "13px"
    },
    md: {
      padding: "13px 26px",
      fontSize: "14px"
    },
    lg: {
      padding: "17px 36px",
      fontSize: "15px"
    }
  };
  const variants = {
    primary: {
      background: "var(--brand)",
      color: "var(--cream)",
      border: "1px solid transparent",
      boxShadow: "var(--shadow-green)"
    },
    secondary: {
      background: "var(--ink-900)",
      color: "var(--cream)",
      border: "1px solid transparent"
    },
    accent: {
      background: "var(--accent)",
      color: "var(--white)",
      border: "1px solid transparent"
    },
    cream: {
      background: "var(--cream)",
      color: "var(--green-800)",
      border: "1px solid transparent"
    },
    ghost: {
      background: "transparent",
      color: "var(--brand)",
      border: "1px solid transparent"
    },
    outline: {
      background: "transparent",
      color: "var(--brand)",
      border: "1px solid var(--brand)"
    },
    outlineLight: {
      background: "transparent",
      color: "var(--cream)",
      border: "1px solid var(--border-dark)"
    }
  };
  const hovers = {
    primary: {
      background: "var(--brand-hover)",
      transform: "translateY(-2px)"
    },
    secondary: {
      background: "var(--ink-700)",
      transform: "translateY(-2px)"
    },
    accent: {
      background: "var(--accent-hover)",
      transform: "translateY(-2px)"
    },
    cream: {
      background: "#fff",
      transform: "translateY(-2px)"
    },
    ghost: {
      background: "var(--brand-soft)"
    },
    outline: {
      background: "var(--brand)",
      color: "var(--cream)"
    },
    outlineLight: {
      background: "var(--cream)",
      color: "var(--green-800)"
    }
  };
  const Tag = as;
  const hov = !disabled && hover ? hovers[variant] : {};
  return /*#__PURE__*/React.createElement(Tag, _extends({
    style: {
      display: "inline-flex",
      alignItems: "center",
      justifyContent: "center",
      gap: "10px",
      fontFamily: "var(--font-body)",
      fontWeight: 600,
      letterSpacing: "0.02em",
      lineHeight: 1,
      borderRadius: "var(--radius-sm)",
      cursor: disabled ? "not-allowed" : "pointer",
      transition: "var(--transition)",
      textDecoration: "none",
      width: full ? "100%" : "auto",
      opacity: disabled ? 0.5 : 1,
      whiteSpace: "nowrap",
      ...sizes[size],
      ...variants[variant],
      ...hov,
      ...style
    },
    disabled: as === "button" ? disabled : undefined,
    onMouseEnter: () => setHover(true),
    onMouseLeave: () => setHover(false)
  }, rest), iconLeft, children, iconRight);
}
Object.assign(__ds_scope, { Button });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Button.jsx", error: String((e && e.message) || e) }); }

// components/core/Eyebrow.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * DOVA Futures — Eyebrow / Kicker
 * Short uppercase label above headlines. Wide-tracked Inter.
 */
function Eyebrow({
  children,
  color = "green700",
  style = {},
  ...rest
}) {
  const colors = {
    green700: "var(--green-700)",
    green300: "var(--green-300)",
    clay: "var(--clay)",
    muted: "var(--text-muted)"
  };
  return /*#__PURE__*/React.createElement("span", _extends({
    style: {
      display: "inline-block",
      fontFamily: "var(--font-body)",
      fontSize: "var(--fs-2xs)",
      fontWeight: 600,
      letterSpacing: "var(--tracking-eyebrow)",
      textTransform: "uppercase",
      color: colors[color] || colors.green700,
      ...style
    }
  }, rest), children);
}
Object.assign(__ds_scope, { Eyebrow });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Eyebrow.jsx", error: String((e && e.message) || e) }); }

// components/core/SectionHeader.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * DOVA Futures — SectionHeader
 * Eyebrow + Bebas display title. The standard heading block for sections.
 */
function SectionHeader({
  eyebrow,
  title,
  onDark = false,
  align = "left",
  eyebrowColor,
  titleSize = "var(--fs-display-lg)",
  style = {},
  ...rest
}) {
  const ebColor = eyebrowColor || (onDark ? "green300" : "green700");
  return /*#__PURE__*/React.createElement("div", _extends({
    style: {
      textAlign: align,
      ...style
    }
  }, rest), eyebrow && /*#__PURE__*/React.createElement("div", {
    style: {
      marginBottom: "16px"
    }
  }, /*#__PURE__*/React.createElement(__ds_scope.Eyebrow, {
    color: ebColor
  }, eyebrow)), /*#__PURE__*/React.createElement("h2", {
    style: {
      fontFamily: "var(--font-display)",
      fontSize: titleSize,
      lineHeight: 1.0,
      letterSpacing: "var(--tracking-display)",
      margin: 0,
      color: onDark ? "var(--cream)" : "var(--text-strong)"
    }
  }, title));
}
Object.assign(__ds_scope, { SectionHeader });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/SectionHeader.jsx", error: String((e && e.message) || e) }); }

// components/core/Stat.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * DOVA Futures — Stat
 * Big-number trust metric. Bebas numeral + uppercase label. `onDark` for green
 * sections, `accent` to color the numeral clay instead of green.
 */
function Stat({
  value,
  label,
  onDark = false,
  accent = false,
  align = "left",
  style = {},
  ...rest
}) {
  const numeralColor = accent ? onDark ? "var(--clay)" : "var(--clay)" : onDark ? "var(--green-300)" : "var(--brand)";
  return /*#__PURE__*/React.createElement("div", _extends({
    style: {
      textAlign: align,
      ...style
    }
  }, rest), /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: "var(--font-display)",
      fontSize: "clamp(40px, 5vw, 64px)",
      lineHeight: 1,
      letterSpacing: "var(--tracking-display)",
      color: numeralColor
    }
  }, value), /*#__PURE__*/React.createElement("div", {
    style: {
      marginTop: "8px",
      fontFamily: "var(--font-body)",
      fontSize: "13px",
      fontWeight: 500,
      letterSpacing: "0.04em",
      textTransform: "uppercase",
      color: onDark ? "var(--text-on-dark-mut)" : "var(--text-muted)"
    }
  }, label));
}
Object.assign(__ds_scope, { Stat });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Stat.jsx", error: String((e && e.message) || e) }); }

// components/core/Tag.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * DOVA Futures — Tag
 * Uppercase outline pill for skills / categories. `onDark` for green sections.
 */
function Tag({
  children,
  onDark = false,
  style = {},
  ...rest
}) {
  return /*#__PURE__*/React.createElement("span", _extends({
    style: {
      display: "inline-flex",
      alignItems: "center",
      fontFamily: "var(--font-body)",
      fontSize: "11px",
      fontWeight: 600,
      letterSpacing: "0.1em",
      textTransform: "uppercase",
      padding: "6px 14px",
      borderRadius: "var(--radius-pill)",
      border: `1px solid ${onDark ? "var(--border-dark)" : "var(--stone)"}`,
      color: onDark ? "var(--green-300)" : "var(--slate)",
      background: "transparent",
      ...style
    }
  }, rest), children);
}
Object.assign(__ds_scope, { Tag });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Tag.jsx", error: String((e && e.message) || e) }); }

// components/forms/Field.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * DOVA Futures — Field
 * Form-row wrapper: label + control (children) + optional hint/error.
 */
function Field({
  label,
  htmlFor,
  hint,
  error,
  className,
  style = {},
  children,
  ...rest
}) {
  return /*#__PURE__*/React.createElement("div", _extends({
    className: className,
    style: {
      display: "flex",
      flexDirection: "column",
      gap: "7px",
      ...style
    }
  }, rest), label && /*#__PURE__*/React.createElement("label", {
    htmlFor: htmlFor,
    style: {
      fontFamily: "var(--font-body)",
      fontSize: "13px",
      fontWeight: 600,
      color: "var(--ink-800)",
      letterSpacing: "0.01em"
    }
  }, label), children, (hint || error) && /*#__PURE__*/React.createElement("span", {
    style: {
      fontSize: "12px",
      color: error ? "var(--danger)" : "var(--text-muted)"
    }
  }, error || hint));
}
Object.assign(__ds_scope, { Field });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/forms/Field.jsx", error: String((e && e.message) || e) }); }

// components/forms/Input.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * DOVA Futures — Input
 * Plain text field with hairline border that turns brand-green on focus.
 * Use inside <Field> for a label. Cream-tinted surface, soft inset.
 */
function Input({
  invalid = false,
  style = {},
  ...rest
}) {
  const [focus, setFocus] = React.useState(false);
  return /*#__PURE__*/React.createElement("input", _extends({
    onFocus: e => {
      setFocus(true);
      rest.onFocus && rest.onFocus(e);
    },
    onBlur: e => {
      setFocus(false);
      rest.onBlur && rest.onBlur(e);
    },
    style: {
      width: "100%",
      boxSizing: "border-box",
      fontFamily: "var(--font-body)",
      fontSize: "15px",
      color: "var(--ink-900)",
      background: "var(--white)",
      border: `1px solid ${invalid ? "var(--danger)" : focus ? "var(--brand)" : "var(--border-light)"}`,
      boxShadow: focus && !invalid ? "0 0 0 3px rgba(53,122,91,0.14)" : "inset 0 1px 2px rgba(26,26,26,0.04)",
      borderRadius: "var(--radius-md)",
      padding: "12px 14px",
      outline: "none",
      transition: "var(--transition)",
      ...style
    }
  }, rest));
}
Object.assign(__ds_scope, { Input });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/forms/Input.jsx", error: String((e && e.message) || e) }); }

// components/forms/Textarea.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * DOVA Futures — Textarea
 * Multi-line field matching <Input>. Green focus ring, vertical resize.
 */
function Textarea({
  invalid = false,
  style = {},
  ...rest
}) {
  const [focus, setFocus] = React.useState(false);
  return /*#__PURE__*/React.createElement("textarea", _extends({
    onFocus: e => {
      setFocus(true);
      rest.onFocus && rest.onFocus(e);
    },
    onBlur: e => {
      setFocus(false);
      rest.onBlur && rest.onBlur(e);
    },
    style: {
      width: "100%",
      boxSizing: "border-box",
      fontFamily: "var(--font-body)",
      fontSize: "15px",
      lineHeight: 1.6,
      color: "var(--ink-900)",
      background: "var(--white)",
      border: `1px solid ${invalid ? "var(--danger)" : focus ? "var(--brand)" : "var(--border-light)"}`,
      boxShadow: focus && !invalid ? "0 0 0 3px rgba(53,122,91,0.14)" : "inset 0 1px 2px rgba(26,26,26,0.04)",
      borderRadius: "var(--radius-md)",
      padding: "12px 14px",
      minHeight: "110px",
      resize: "vertical",
      outline: "none",
      transition: "var(--transition)",
      ...style
    }
  }, rest));
}
Object.assign(__ds_scope, { Textarea });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/forms/Textarea.jsx", error: String((e && e.message) || e) }); }

// components/surfaces/Card.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * DOVA Futures — Card. Generic surface with hairline border + soft shadow,
 * lifts on hover. Works on light (default) or dark-green sections.
 */
function Card({
  children,
  onDark = false,
  hover = true,
  padding = "28px",
  style = {},
  ...rest
}) {
  const base = {
    background: onDark ? "rgba(245,239,232,0.04)" : "var(--surface-card)",
    border: `1px solid ${onDark ? "var(--border-dark)" : "var(--border-light)"}`,
    borderRadius: "var(--radius-lg)",
    padding,
    boxShadow: onDark ? "none" : "var(--shadow-sm)",
    transition: "var(--transition)",
    ...style
  };
  return /*#__PURE__*/React.createElement("div", _extends({
    style: base,
    onMouseEnter: e => {
      if (!hover) return;
      e.currentTarget.style.transform = "translateY(-4px)";
      e.currentTarget.style.boxShadow = onDark ? "var(--shadow-green)" : "var(--shadow-lg)";
      if (onDark) e.currentTarget.style.borderColor = "rgba(143,196,169,0.3)";
    },
    onMouseLeave: e => {
      if (!hover) return;
      e.currentTarget.style.transform = "none";
      e.currentTarget.style.boxShadow = onDark ? "none" : "var(--shadow-sm)";
      e.currentTarget.style.borderColor = onDark ? "var(--border-dark)" : "var(--border-light)";
    }
  }, rest), children);
}

/**
 * ServiceCard — icon-in-a-framed-box + title + description.
 * Mirrors the website's service tiles. Top accent rule by default.
 */
function ServiceCard({
  icon,
  title,
  children,
  onDark = true,
  style = {}
}) {
  return /*#__PURE__*/React.createElement(Card, {
    onDark: onDark,
    padding: "36px",
    style: style
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      width: "60px",
      height: "60px",
      border: `1px solid ${onDark ? "var(--border-dark)" : "var(--border-light)"}`,
      borderRadius: "var(--radius-sm)",
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      marginBottom: "24px",
      color: onDark ? "var(--green-300)" : "var(--brand)"
    }
  }, icon), /*#__PURE__*/React.createElement("h3", {
    style: {
      fontFamily: "var(--font-display)",
      fontSize: "28px",
      letterSpacing: "0.02em",
      lineHeight: 1,
      margin: "0 0 12px",
      color: onDark ? "var(--cream)" : "var(--text-strong)"
    }
  }, title), /*#__PURE__*/React.createElement("p", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: "15px",
      lineHeight: 1.65,
      margin: 0,
      color: onDark ? "var(--text-on-dark-mut)" : "var(--text-body)"
    }
  }, children));
}

/**
 * ProjectCard — 4:3 image with bottom protection gradient, category overlay tag,
 * and a caption that slides up on hover.
 */
function ProjectCard({
  image,
  category,
  title,
  location,
  style = {}
}) {
  return /*#__PURE__*/React.createElement("div", {
    style: {
      position: "relative",
      overflow: "hidden",
      aspectRatio: "4 / 3",
      borderRadius: "var(--radius-lg)",
      background: "var(--green-900)",
      cursor: "pointer",
      ...style
    },
    onMouseEnter: e => {
      const c = e.currentTarget.querySelector(".dova-pc-cap");
      if (c) {
        c.style.transform = "translateY(0)";
        c.style.opacity = "1";
      }
    },
    onMouseLeave: e => {
      const c = e.currentTarget.querySelector(".dova-pc-cap");
      if (c) {
        c.style.transform = "translateY(14px)";
        c.style.opacity = "0";
      }
    }
  }, /*#__PURE__*/React.createElement("img", {
    src: image,
    alt: title,
    style: {
      position: "absolute",
      inset: 0,
      width: "100%",
      height: "100%",
      objectFit: "cover"
    }
  }), /*#__PURE__*/React.createElement("div", {
    style: {
      position: "absolute",
      inset: 0,
      background: "var(--overlay-bottom)"
    }
  }), category && /*#__PURE__*/React.createElement("span", {
    style: {
      position: "absolute",
      top: "16px",
      left: "16px",
      fontFamily: "var(--font-body)",
      fontSize: "10px",
      fontWeight: 600,
      letterSpacing: "0.14em",
      textTransform: "uppercase",
      padding: "5px 12px",
      borderRadius: "var(--radius-pill)",
      background: "var(--accent)",
      color: "#fff"
    }
  }, category), /*#__PURE__*/React.createElement("div", {
    className: "dova-pc-cap",
    style: {
      position: "absolute",
      left: 0,
      right: 0,
      bottom: 0,
      padding: "24px",
      transform: "translateY(14px)",
      opacity: 0,
      transition: "var(--transition)"
    }
  }, /*#__PURE__*/React.createElement("h3", {
    style: {
      fontFamily: "var(--font-display)",
      fontSize: "24px",
      letterSpacing: "0.02em",
      color: "var(--cream)",
      margin: "0 0 4px"
    }
  }, title), location && /*#__PURE__*/React.createElement("p", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: "13px",
      color: "var(--text-on-dark-mut)",
      margin: 0
    }
  }, location)));
}
Object.assign(__ds_scope, { Card, ServiceCard, ProjectCard });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/surfaces/Card.jsx", error: String((e && e.message) || e) }); }

// ui_kits/dova-website/pages.jsx
try { (() => {
/* DOVA Futures website — page bodies. */
const {
  Button: DButton,
  Eyebrow: DEyebrow,
  SectionHeader: DSH,
  ServiceCard: DServiceCard,
  ProjectCard: DProjectCard,
  Stat: DStat,
  Field: DField,
  Input: DInput,
  Textarea: DTextarea,
  Tag: DTag,
  Badge: DBadge
} = window.DOVAFuturesDesignSystem_0aa9ec;
const {
  Section: S,
  HeroReveal: DHero,
  icons: I,
  AFTER: IMG_AFTER,
  BEFORE: IMG_BEFORE
} = window.DovaScreens;
function Home({
  go
}) {
  return /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("section", {
    style: {
      position: "relative",
      minHeight: "88vh",
      display: "flex",
      alignItems: "center",
      backgroundImage: "linear-gradient(var(--grid-line) 1px,transparent 1px),linear-gradient(90deg,var(--grid-line) 1px,transparent 1px)",
      backgroundSize: "60px 60px",
      background: "var(--green-900)"
    }
  }, /*#__PURE__*/React.createElement(DHero, null), /*#__PURE__*/React.createElement("div", {
    style: {
      position: "relative",
      zIndex: 10,
      maxWidth: "var(--container-max)",
      margin: "0 auto",
      padding: "120px var(--container-pad) 80px",
      width: "100%"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      maxWidth: "760px"
    }
  }, /*#__PURE__*/React.createElement(DEyebrow, {
    color: "green300",
    style: {
      marginBottom: "22px"
    }
  }, "Design\u2013Build Excellence"), /*#__PURE__*/React.createElement("h1", {
    style: {
      fontFamily: "var(--font-display)",
      fontSize: "var(--fs-display-2xl)",
      lineHeight: 0.92,
      letterSpacing: "0.02em",
      color: "var(--cream)",
      margin: "0 0 26px"
    }
  }, "DESIGNED WITH INTENT.", /*#__PURE__*/React.createElement("br", null), "BUILT WITH PRECISION."), /*#__PURE__*/React.createElement("p", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: "var(--fs-lg)",
      fontWeight: 300,
      lineHeight: 1.6,
      color: "var(--text-on-dark)",
      maxWidth: "520px",
      margin: "0 0 38px"
    }
  }, "Rethink the future \u2014 integrated design and construction excellence, engineered for precision across Nigeria."), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      gap: "14px",
      flexWrap: "wrap"
    }
  }, /*#__PURE__*/React.createElement(DButton, {
    variant: "cream",
    size: "lg",
    onClick: () => go("contact")
  }, "Start Your Project"), /*#__PURE__*/React.createElement(DButton, {
    variant: "outlineLight",
    size: "lg",
    onClick: () => go("projects")
  }, "View Portfolio"))))), /*#__PURE__*/React.createElement(S, {
    dark: true
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: "grid",
      gridTemplateColumns: "1fr 1fr",
      gap: "64px",
      alignItems: "center"
    }
  }, /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement(DSH, {
    onDark: true,
    eyebrow: "Who We Are",
    title: "BUILDING TOMORROW'S LANDMARKS"
  }), /*#__PURE__*/React.createElement("p", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: "17px",
      lineHeight: 1.75,
      color: "var(--text-on-dark-mut)",
      margin: "24px 0 18px"
    }
  }, "DOVA Futures is a premier design\u2013build construction company delivering exceptional architectural and construction services. We combine innovative design with superior craftsmanship to transform ambitious visions into remarkable structures."), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      gap: "48px",
      marginTop: "34px"
    }
  }, /*#__PURE__*/React.createElement(DStat, {
    value: "20+",
    label: "Sites managed",
    onDark: true
  }), /*#__PURE__*/React.createElement(DStat, {
    value: "\u20A6350M+",
    label: "Project value",
    onDark: true,
    accent: true
  }), /*#__PURE__*/React.createElement(DStat, {
    value: "5+",
    label: "Years delivering",
    onDark: true
  }))), /*#__PURE__*/React.createElement("div", {
    style: {
      position: "relative"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      aspectRatio: "1/1",
      borderRadius: "var(--radius-lg)",
      overflow: "hidden",
      border: "1px solid var(--border-dark)"
    }
  }, /*#__PURE__*/React.createElement("img", {
    src: IMG_AFTER,
    alt: "DOVA project",
    style: {
      width: "100%",
      height: "100%",
      objectFit: "cover"
    }
  })), /*#__PURE__*/React.createElement("div", {
    style: {
      position: "absolute",
      bottom: "-22px",
      right: "-22px",
      width: "120px",
      height: "120px",
      border: "1px solid var(--border-dark)"
    }
  })))), /*#__PURE__*/React.createElement(S, {
    grid: true
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      textAlign: "center",
      marginBottom: "56px"
    }
  }, /*#__PURE__*/React.createElement(DSH, {
    align: "center",
    onDark: true,
    eyebrow: "What We Do",
    title: "OUR CORE SERVICES"
  })), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "grid",
      gridTemplateColumns: "repeat(3,1fr)",
      gap: "22px"
    }
  }, /*#__PURE__*/React.createElement(DServiceCard, {
    icon: I.plan,
    title: "Architectural Planning"
  }, "Comprehensive design from concept development through detailed construction documentation."), /*#__PURE__*/React.createElement(DServiceCard, {
    icon: I.build,
    title: "Building Construction"
  }, "Full-scale construction with rigorous quality control, timeline management, and transparent budgeting."), /*#__PURE__*/React.createElement(DServiceCard, {
    icon: I.interior,
    title: "Interior Finishing"
  }, "High-end interior fit-outs that transform spaces into sophisticated, functional environments."))), /*#__PURE__*/React.createElement(S, {
    cream: true
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: "grid",
      gridTemplateColumns: "1fr 1fr",
      gap: "64px",
      alignItems: "center"
    }
  }, /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement(DSH, {
    eyebrow: "The Difference",
    eyebrowColor: "clay",
    title: "DESIGN & BUILD UNDER ONE ROOF"
  }), /*#__PURE__*/React.createElement("p", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: "17px",
      lineHeight: 1.75,
      color: "var(--text-body)",
      margin: "24px 0 26px"
    }
  }, "We eliminate the disconnect between architectural drawings and on-site execution. Every design is engineered to be built exactly as envisioned \u2014 without compromise, delay, or cost escalation."), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      flexDirection: "column",
      gap: "14px"
    }
  }, ["Unified design-build methodology", "Streamlined approval processes", "Reduced timeline and cost overruns", "Direct accountability for outcomes"].map(t => /*#__PURE__*/React.createElement("div", {
    key: t,
    style: {
      display: "flex",
      alignItems: "center",
      gap: "14px"
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      width: "26px",
      height: "26px",
      borderRadius: "50%",
      background: "var(--brand)",
      color: "var(--cream)",
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      flexShrink: 0,
      fontSize: "13px"
    }
  }, "\u2713"), /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: "16px",
      color: "var(--ink-900)"
    }
  }, t))))), /*#__PURE__*/React.createElement("div", {
    style: {
      aspectRatio: "4/5",
      borderRadius: "var(--radius-lg)",
      overflow: "hidden",
      border: "2px solid var(--ink-900)"
    }
  }, /*#__PURE__*/React.createElement("img", {
    src: IMG_AFTER,
    alt: "DOVA build",
    style: {
      width: "100%",
      height: "100%",
      objectFit: "cover"
    }
  })))), /*#__PURE__*/React.createElement(S, {
    dark: true,
    grid: true
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      textAlign: "center",
      marginBottom: "56px"
    }
  }, /*#__PURE__*/React.createElement(DSH, {
    align: "center",
    onDark: true,
    eyebrow: "How We Work",
    title: "OUR 5-STEP PROCESS"
  })), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "grid",
      gridTemplateColumns: "repeat(5,1fr)",
      gap: "16px"
    }
  }, [["01", "Consultation"], ["02", "Design"], ["03", "Engineering"], ["04", "Construction"], ["05", "Handover"]].map(([n, t]) => /*#__PURE__*/React.createElement("div", {
    key: n,
    style: {
      textAlign: "center"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      width: "52px",
      height: "52px",
      borderRadius: "50%",
      border: "1px solid var(--border-dark)",
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      margin: "0 auto 18px",
      fontFamily: "var(--font-display)",
      fontSize: "20px",
      color: "var(--green-300)"
    }
  }, n), /*#__PURE__*/React.createElement("h3", {
    style: {
      fontFamily: "var(--font-display)",
      fontSize: "24px",
      letterSpacing: "0.02em",
      color: "var(--cream)",
      margin: "0 0 6px"
    }
  }, t))))), /*#__PURE__*/React.createElement(CTA, {
    go: go
  }), /*#__PURE__*/React.createElement(Footer, null));
}
function Projects({
  go
}) {
  const items = [["Commercial", "The Body Shop Fit-Out", "Ikeja, Lagos"], ["Infrastructure", "Palm Oil Drainage Works", "Akure, Ondo"], ["Residential", "Residential Duplex", "Lagos"], ["Interiors", "Ado Hall Renovation", "Ekiti State"], ["Commercial", "Market Infrastructure", "Edo State"], ["Infrastructure", "Structural Works", "Multi-State"]];
  const [filter, setFilter] = useState("All");
  const cats = ["All", "Residential", "Commercial", "Infrastructure", "Interiors"];
  const shown = items.filter(p => filter === "All" || p[0] === filter);
  return /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement(S, {
    dark: true,
    grid: true,
    style: {
      paddingTop: "80px"
    }
  }, /*#__PURE__*/React.createElement(DSH, {
    onDark: true,
    eyebrow: "Portfolio",
    title: "OUR PROJECTS"
  }), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      gap: "10px",
      flexWrap: "wrap",
      margin: "34px 0 40px"
    }
  }, cats.map(c => /*#__PURE__*/React.createElement("button", {
    key: c,
    onClick: () => setFilter(c),
    style: {
      fontFamily: "var(--font-body)",
      fontSize: "13px",
      letterSpacing: "0.04em",
      padding: "9px 18px",
      borderRadius: "var(--radius-sm)",
      cursor: "pointer",
      transition: "var(--transition)",
      background: filter === c ? "var(--cream)" : "transparent",
      color: filter === c ? "var(--green-800)" : "var(--text-on-dark)",
      border: `1px solid ${filter === c ? "var(--cream)" : "var(--border-dark)"}`
    }
  }, c))), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "grid",
      gridTemplateColumns: "repeat(3,1fr)",
      gap: "22px"
    }
  }, shown.map((p, i) => /*#__PURE__*/React.createElement(DProjectCard, {
    key: i,
    image: IMG_AFTER,
    category: p[0],
    title: p[1],
    location: p[2]
  })))), /*#__PURE__*/React.createElement(CTA, {
    go: go
  }), /*#__PURE__*/React.createElement(Footer, null));
}
function Contact() {
  const [sent, setSent] = useState(false);
  return /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement(S, {
    cream: true,
    style: {
      minHeight: "70vh"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: "grid",
      gridTemplateColumns: "1fr 1fr",
      gap: "72px",
      alignItems: "start"
    }
  }, /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement(DSH, {
    eyebrow: "Get In Touch",
    eyebrowColor: "clay",
    title: "LET'S BUILD IT PROPERLY."
  }), /*#__PURE__*/React.createElement("p", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: "18px",
      lineHeight: 1.7,
      color: "var(--text-body)",
      margin: "22px 0 32px"
    }
  }, "Ready to transform your vision into reality? Tell us about your project and we'll be in touch."), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      flexDirection: "column",
      gap: "16px"
    }
  }, [["Phone", "+234 816 367 5439"], ["Email", "info@dovafutures.com"], ["Location", "Lagos, Nigeria"]].map(([l, v]) => /*#__PURE__*/React.createElement("div", {
    key: l
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: "11px",
      fontWeight: 600,
      letterSpacing: "0.15em",
      textTransform: "uppercase",
      color: "var(--clay)"
    }
  }, l), /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: "16px",
      color: "var(--ink-900)",
      marginTop: "3px"
    }
  }, v))))), /*#__PURE__*/React.createElement("div", {
    style: {
      background: "var(--white)",
      border: "1px solid var(--border-light)",
      borderRadius: "var(--radius-lg)",
      padding: "36px",
      boxShadow: "var(--shadow-md)"
    }
  }, sent ? /*#__PURE__*/React.createElement("div", {
    style: {
      textAlign: "center",
      padding: "40px 0"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: "var(--font-display)",
      fontSize: "40px",
      color: "var(--brand)",
      letterSpacing: "0.02em"
    }
  }, "THANK YOU"), /*#__PURE__*/React.createElement("p", {
    style: {
      fontFamily: "var(--font-body)",
      color: "var(--text-body)",
      marginTop: "8px"
    }
  }, "We'll respond within one business day.")) : /*#__PURE__*/React.createElement("form", {
    onSubmit: e => {
      e.preventDefault();
      setSent(true);
    },
    style: {
      display: "grid",
      gridTemplateColumns: "1fr 1fr",
      gap: "18px"
    }
  }, /*#__PURE__*/React.createElement(DField, {
    label: "Full name"
  }, /*#__PURE__*/React.createElement(DInput, {
    required: true,
    placeholder: "Jane Adeyemi"
  })), /*#__PURE__*/React.createElement(DField, {
    label: "Phone"
  }, /*#__PURE__*/React.createElement(DInput, {
    placeholder: "+234 \u2026"
  })), /*#__PURE__*/React.createElement(DField, {
    label: "Email",
    style: {
      gridColumn: "1 / -1"
    }
  }, /*#__PURE__*/React.createElement(DInput, {
    type: "email",
    required: true,
    placeholder: "you@company.com"
  })), /*#__PURE__*/React.createElement(DField, {
    label: "Project details",
    style: {
      gridColumn: "1 / -1"
    }
  }, /*#__PURE__*/React.createElement(DTextarea, {
    rows: 4,
    placeholder: "Scope, location & timeline\u2026"
  })), /*#__PURE__*/React.createElement("div", {
    style: {
      gridColumn: "1 / -1",
      display: "flex",
      gap: "12px"
    }
  }, /*#__PURE__*/React.createElement(DButton, {
    variant: "primary",
    type: "submit"
  }, "Send Enquiry"), /*#__PURE__*/React.createElement(DButton, {
    variant: "secondary",
    type: "button"
  }, "Send via WhatsApp")))))), /*#__PURE__*/React.createElement(Footer, null));
}
function CTA({
  go
}) {
  return /*#__PURE__*/React.createElement(S, {
    cream: true
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      textAlign: "center",
      maxWidth: "760px",
      margin: "0 auto"
    }
  }, /*#__PURE__*/React.createElement("h2", {
    style: {
      fontFamily: "var(--font-display)",
      fontSize: "var(--fs-display-xl)",
      letterSpacing: "0.02em",
      color: "var(--ink-900)",
      margin: "0 0 18px"
    }
  }, "READY TO START?"), /*#__PURE__*/React.createElement("p", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: "18px",
      color: "var(--text-body)",
      margin: "0 0 32px"
    }
  }, "Let's discuss your project and explore the possibilities together."), /*#__PURE__*/React.createElement(DButton, {
    variant: "primary",
    size: "lg",
    onClick: () => go("contact")
  }, "Start Your Project")));
}
function Footer() {
  return /*#__PURE__*/React.createElement("footer", {
    style: {
      background: "var(--green-950)",
      padding: "40px var(--container-pad)",
      borderTop: "1px solid var(--border-dark)"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      maxWidth: "var(--container-max)",
      margin: "0 auto",
      display: "flex",
      justifyContent: "space-between",
      alignItems: "center",
      flexWrap: "wrap",
      gap: "16px"
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-display)",
      fontSize: "22px",
      letterSpacing: "0.08em",
      color: "var(--cream)"
    }
  }, "DOVA FUTURES DEVELOPERS"), /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: "13px",
      color: "var(--text-on-dark-mut)"
    }
  }, "\xA9 2025 DOVA Futures Developers. All Rights Reserved.")));
}
window.DovaPages = {
  Home,
  Projects,
  Contact
};
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/dova-website/pages.jsx", error: String((e && e.message) || e) }); }

// ui_kits/dova-website/screens.jsx
try { (() => {
/* DOVA Futures website — UI kit screens. Exposes components on window. */
const {
  Button,
  Eyebrow,
  SectionHeader,
  ServiceCard,
  ProjectCard,
  Stat,
  Field,
  Input,
  Textarea,
  Tag,
  Badge
} = window.DOVAFuturesDesignSystem_0aa9ec;
const {
  useState,
  useRef,
  useEffect
} = React;
const ASSET = "../../assets";
const AFTER = ASSET + "/projects/ado-hall/after.png";
const BEFORE = ASSET + "/projects/ado-hall/before.jpg";

/* ---- line icons (1.5px, 24-grid) ---- */
const Icon = ({
  d,
  size = 28
}) => /*#__PURE__*/React.createElement("svg", {
  width: size,
  height: size,
  viewBox: "0 0 24 24",
  fill: "none",
  stroke: "currentColor",
  strokeWidth: "1.5",
  strokeLinecap: "round",
  strokeLinejoin: "round"
}, d);
const icons = {
  plan: /*#__PURE__*/React.createElement(Icon, {
    d: /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("path", {
      d: "M3 21h18M3 7v14M21 7v14M6 7V3h12v4M9 11h6M9 15h6"
    }))
  }),
  build: /*#__PURE__*/React.createElement(Icon, {
    d: /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("path", {
      d: "M2 20h20M4 20V8l8-6l8 6v12M9 20v-6h6v6"
    }))
  }),
  interior: /*#__PURE__*/React.createElement(Icon, {
    d: /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("rect", {
      x: "3",
      y: "3",
      width: "18",
      height: "18",
      rx: "1"
    }), /*#__PURE__*/React.createElement("path", {
      d: "M3 9h18M9 21V9"
    }))
  }),
  manage: /*#__PURE__*/React.createElement(Icon, {
    d: /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("path", {
      d: "M9 11l3 3 8-8M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"
    }))
  }),
  shield: /*#__PURE__*/React.createElement(Icon, {
    size: 24,
    d: /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("path", {
      d: "M12 2L3 6v6c0 5 3.8 8.5 9 10 5.2-1.5 9-5 9-10V6l-9-4z"
    }))
  }),
  clock: /*#__PURE__*/React.createElement(Icon, {
    size: 24,
    d: /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("circle", {
      cx: "12",
      cy: "12",
      r: "9"
    }), /*#__PURE__*/React.createElement("path", {
      d: "M12 7v5l3 2"
    }))
  }),
  layers: /*#__PURE__*/React.createElement(Icon, {
    size: 24,
    d: /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("path", {
      d: "M12 2 2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"
    }))
  }),
  star: /*#__PURE__*/React.createElement(Icon, {
    size: 24,
    d: /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("polygon", {
      points: "12 2 15 9 22 9.3 16.5 14 18.5 21 12 17 5.5 21 7.5 14 2 9.3 9 9"
    }))
  })
};
const WORDMARK = ASSET + "/logo/DOVA Logo - W.png";

/* ---- Navigation ---- */
function Nav({
  page,
  go
}) {
  const links = [["home", "Home"], ["services", "Services"], ["projects", "Projects"], ["contact", "Contact"]];
  return /*#__PURE__*/React.createElement("nav", {
    style: {
      position: "sticky",
      top: 0,
      zIndex: 50,
      height: "76px",
      display: "flex",
      alignItems: "center",
      background: "rgba(16,42,32,0.86)",
      backdropFilter: "var(--backdrop-blur)",
      borderBottom: "1px solid var(--border-dark)"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      maxWidth: "var(--container-max)",
      margin: "0 auto",
      padding: "0 var(--container-pad)",
      width: "100%",
      display: "flex",
      alignItems: "center",
      justifyContent: "space-between"
    }
  }, /*#__PURE__*/React.createElement("a", {
    href: "#",
    onClick: e => {
      e.preventDefault();
      go("home");
    },
    style: {
      display: "flex",
      alignItems: "center"
    }
  }, /*#__PURE__*/React.createElement("img", {
    src: WORDMARK,
    alt: "DOVA Futures",
    style: {
      height: "46px",
      width: "auto"
    }
  })), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      alignItems: "center",
      gap: "34px"
    }
  }, links.map(([id, label]) => /*#__PURE__*/React.createElement("a", {
    key: id,
    href: "#",
    onClick: e => {
      e.preventDefault();
      go(id);
    },
    style: {
      fontFamily: "var(--font-body)",
      fontSize: "14px",
      letterSpacing: "0.04em",
      color: page === id ? "var(--green-300)" : "var(--text-on-dark)",
      textDecoration: "none",
      fontWeight: page === id ? 600 : 400
    }
  }, label)), /*#__PURE__*/React.createElement(Button, {
    variant: "cream",
    size: "sm",
    onClick: () => go("contact")
  }, "Start a Project"))));
}

/* ---- Hero before/after reveal ---- */
function HeroReveal() {
  const [split, setSplit] = useState(52);
  const ref = useRef(null);
  const drag = useRef(false);
  useEffect(() => {
    const move = e => {
      if (!drag.current || !ref.current) return;
      const r = ref.current.getBoundingClientRect();
      const x = (e.touches ? e.touches[0].clientX : e.clientX) - r.left;
      setSplit(Math.max(6, Math.min(94, x / r.width * 100)));
    };
    const up = () => drag.current = false;
    window.addEventListener("mousemove", move);
    window.addEventListener("mouseup", up);
    window.addEventListener("touchmove", move);
    window.addEventListener("touchend", up);
    return () => {
      window.removeEventListener("mousemove", move);
      window.removeEventListener("mouseup", up);
      window.removeEventListener("touchmove", move);
      window.removeEventListener("touchend", up);
    };
  }, []);
  return /*#__PURE__*/React.createElement("div", {
    ref: ref,
    style: {
      position: "absolute",
      inset: 0,
      overflow: "hidden"
    }
  }, /*#__PURE__*/React.createElement("img", {
    src: AFTER,
    alt: "Rendered",
    style: {
      position: "absolute",
      inset: 0,
      width: "100%",
      height: "100%",
      objectFit: "cover",
      opacity: 0.55
    }
  }), /*#__PURE__*/React.createElement("div", {
    style: {
      position: "absolute",
      inset: 0,
      clipPath: `inset(0 ${100 - split}% 0 0)`
    }
  }, /*#__PURE__*/React.createElement("img", {
    src: BEFORE,
    alt: "Draft",
    style: {
      width: "100%",
      height: "100%",
      objectFit: "cover",
      opacity: 0.45,
      filter: "grayscale(0.4)"
    }
  })), /*#__PURE__*/React.createElement("div", {
    style: {
      position: "absolute",
      inset: 0,
      background: "var(--overlay-hero)"
    }
  }), /*#__PURE__*/React.createElement("div", {
    onMouseDown: () => drag.current = true,
    onTouchStart: () => drag.current = true,
    style: {
      position: "absolute",
      top: 0,
      bottom: 0,
      left: `${split}%`,
      width: "2px",
      background: "rgba(245,239,232,0.8)",
      transform: "translateX(-50%)",
      cursor: "ew-resize",
      zIndex: 3
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      position: "absolute",
      top: "50%",
      left: "50%",
      transform: "translate(-50%,-50%)",
      width: "44px",
      height: "44px",
      borderRadius: "50%",
      background: "var(--cream)",
      color: "var(--green-800)",
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      boxShadow: "var(--shadow-lg)",
      fontSize: "18px"
    }
  }, "\u21D4"), /*#__PURE__*/React.createElement("span", {
    style: {
      position: "absolute",
      top: "50%",
      right: "calc(100% + 14px)",
      transform: "translateY(-50%)",
      fontSize: "11px",
      letterSpacing: "0.15em",
      textTransform: "uppercase",
      color: "var(--text-on-dark-mut)",
      whiteSpace: "nowrap"
    }
  }, "Draft"), /*#__PURE__*/React.createElement("span", {
    style: {
      position: "absolute",
      top: "50%",
      left: "calc(100% + 14px)",
      transform: "translateY(-50%)",
      fontSize: "11px",
      letterSpacing: "0.15em",
      textTransform: "uppercase",
      color: "var(--text-on-dark-mut)",
      whiteSpace: "nowrap"
    }
  }, "Render")));
}
const Section = ({
  children,
  dark,
  cream,
  grid,
  style
}) => /*#__PURE__*/React.createElement("section", {
  style: {
    padding: "var(--section-pad-y) 0",
    background: cream ? "var(--cream)" : dark ? "var(--green-800)" : "var(--green-900)",
    backgroundImage: grid ? "linear-gradient(var(--grid-line) 1px,transparent 1px),linear-gradient(90deg,var(--grid-line) 1px,transparent 1px)" : "none",
    backgroundSize: grid ? "60px 60px" : "auto",
    ...style
  }
}, /*#__PURE__*/React.createElement("div", {
  style: {
    maxWidth: "var(--container-max)",
    margin: "0 auto",
    padding: "0 var(--container-pad)"
  }
}, children));
window.DovaScreens = {
  Nav,
  HeroReveal,
  Section,
  icons,
  ASSET,
  AFTER,
  BEFORE
};
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/dova-website/screens.jsx", error: String((e && e.message) || e) }); }

__ds_ns.Badge = __ds_scope.Badge;

__ds_ns.Button = __ds_scope.Button;

__ds_ns.Eyebrow = __ds_scope.Eyebrow;

__ds_ns.SectionHeader = __ds_scope.SectionHeader;

__ds_ns.Stat = __ds_scope.Stat;

__ds_ns.Tag = __ds_scope.Tag;

__ds_ns.Field = __ds_scope.Field;

__ds_ns.Input = __ds_scope.Input;

__ds_ns.Textarea = __ds_scope.Textarea;

__ds_ns.Card = __ds_scope.Card;

__ds_ns.ServiceCard = __ds_scope.ServiceCard;

__ds_ns.ProjectCard = __ds_scope.ProjectCard;

})();
