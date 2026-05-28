const ProjectDetail = () => {
    return (
        <div className="min-h-screen bg-gradient-to-br from-slate-50 via-white to-slate-100 px-4 py-10 flex items-center justify-center">
            <div className="w-full max-w-lg rounded-3xl border border-slate-200 bg-white/90 p-8 shadow-[0_20px_60px_-30px_rgba(15,23,42,0.35)] backdrop-blur-sm sm:p-10">
                <div className="mb-6 flex items-center gap-3">
                    <div className="h-3 w-3 rounded-full bg-slate-300" />
                    <div className="h-3 w-3 rounded-full bg-slate-200" />
                    <div className="h-3 w-3 rounded-full bg-slate-300" />
                </div>

                <span className="inline-flex rounded-full border border-slate-200 bg-slate-50 px-3 py-1 text-xs font-medium tracking-wide text-slate-500">
                    UI CHECK
                </span>

                <h1 className="mt-4 text-3xl font-semibold tracking-tight text-slate-900 sm:text-4xl">
                    React + Tailwind is working
                </h1>

                <p className="mt-4 text-base leading-7 text-slate-600 sm:text-lg">
                    If you can see this clean white card with soft shadows, rounded corners,
                    and calm neutral colors, then <strong>React</strong> and <strong>Tailwind CSS</strong> are running correctly.
                </p>

                <div className="mt-8 flex flex-wrap gap-3">
                    <button className="rounded-full bg-slate-900 px-5 py-2.5 text-sm font-medium text-white transition hover:bg-slate-800 focus:outline-none focus:ring-2 focus:ring-slate-400 focus:ring-offset-2">
                        Looks good
                    </button>
                    <button className="rounded-full border border-slate-200 bg-white px-5 py-2.5 text-sm font-medium text-slate-700 transition hover:bg-slate-50 focus:outline-none focus:ring-2 focus:ring-slate-300 focus:ring-offset-2">
                        Check again
                    </button>
                </div>
            </div>
        </div>
    );
};

export default ProjectDetail;
