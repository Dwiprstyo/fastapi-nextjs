const nextConfig = {
  async rewrites() {
    return [
      {
        source: '/api/:path*',
        destination:
          process.env.NODE_ENV === 'development'
            ? 'http://127.0.0.1:8000/api/:path*' // Development endpoint
            : 'http://127.0.0.1:8000/api/:path*', // Production endpoint
      },
      {
        source: '/docs',
        destination:
          process.env.NODE_ENV === 'development'
            ? 'http://127.0.0.1:8000/docs' // Development endpoint
            : '/api/docs', // Production endpoint
      },
      {
        source: '/openapi.json',
        destination:
          process.env.NODE_ENV === 'development'
            ? 'http://127.0.0.1:8000/openapi.json' // Development endpoint
            : '/api/openapi.json', // Production endpoint
      },
    ];
  },
};

module.exports = nextConfig;
