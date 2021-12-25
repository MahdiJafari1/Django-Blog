module.exports = {
    future: {
        removeDeprecatedGapUtilities: true,
        purgeLayersByDefault: true,
    },
    content: {
        content: [
            '../**/templates/*.html',
            '../**/templates/**/*.html'
        ]
    },
    theme: {
        extend: {},
    },
    variants: {},
    plugins: [],
}