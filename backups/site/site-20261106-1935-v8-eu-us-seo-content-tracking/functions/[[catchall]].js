export async function onRequest(context) {
  const { request, env } = context;
  const url = new URL(request.url);
  if (url.hostname === "kalistorik.pages.dev") {
    return Response.redirect("https://kalistorik.com" + url.pathname + url.search, 301);
  }
  const asset = await env.ASSETS.fetch(request);
  if (asset.status !== 404) return asset;
  const notFound = await env.ASSETS.fetch(new URL("/404.html", request.url));
  return new Response(await notFound.text(), {
    status: 404,
    headers: { "Content-Type": "text/html;charset=UTF-8" }
  });
}
