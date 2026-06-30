export async function onRequest(context) {
  const { request, env } = context;
  const asset = await env.ASSETS.fetch(request);
  if (asset.status !== 404) return asset;
  const notFound = await env.ASSETS.fetch(new URL("/404.html", request.url));
  return new Response(await notFound.text(), {
    status: 404,
    headers: { "Content-Type": "text/html;charset=UTF-8" }
  });
}
