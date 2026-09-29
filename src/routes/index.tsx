import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/")({
  head: () => ({
    meta: [
      { title: "SEO Writing Workspace | Alim Karim" },
      {
        name: "description",
        content: "Medium-ready SEO writing and scorecards for Alim Karim.",
      },
      { property: "og:title", content: "SEO Writing Workspace | Alim Karim" },
      {
        property: "og:description",
        content: "Medium-ready SEO writing and scorecards for Alim Karim.",
      },
      { property: "og:type", content: "website" },
      { name: "twitter:card", content: "summary" },
    ],
  }),
  component: Index,
});

function Index() {
  return (
    <main className="min-h-screen bg-background px-6 py-20 text-foreground">
      <div className="mx-auto max-w-2xl">
        <p className="text-sm font-medium uppercase text-muted-foreground">SEO writing workspace</p>
        <h1 className="mt-3 text-4xl font-semibold">Medium-ready writing for Alim Karim</h1>
        <p className="mt-5 max-w-xl text-lg leading-8 text-muted-foreground">
          Articles, publication-ready copies, and detailed scorecards are organized together for review.
        </p>
        <div className="mt-12 border-t border-border pt-8">
          <p className="text-sm text-muted-foreground">Current article</p>
          <h2 className="mt-2 text-2xl font-semibold">It&apos;s Been a Crazy Wake-Up Night</h2>
          <p className="mt-3 leading-7 text-muted-foreground">
            Revised with descriptive links, digit-based number formatting, and a rendered copy for Medium.
          </p>
        </div>
      </div>
    </main>
  );
}
