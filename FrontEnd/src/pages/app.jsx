import { useQuery } from '@tanstack/react-query';

import { buildIconUrl, getProjects } from '../service/api';

const formatDateRange = (startDate, endDate) => {
    if (!startDate && !endDate) {
        return 'No schedule';
    }
    if (!endDate) {
        return `Starts ${startDate}`;
    }
    return `${startDate} → ${endDate}`;
};

const ProjectCard = ({ project }) => {
    const tools = project.tools ?? [];

    return (
        <article className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm transition hover:-translate-y-0.5 hover:shadow-md">
            <div className="flex flex-wrap items-start justify-between gap-3">
                <div>
                    <p className="text-xs font-semibold uppercase tracking-wide text-slate-500">
                        {project.status || 'Status pending'}
                    </p>
                    <h2 className="mt-2 text-xl font-semibold text-slate-900">
                        {project.title}
                    </h2>
                    <p className="mt-2 text-sm text-slate-500">
                        {project.location || 'Location not set'}
                    </p>
                </div>
                <span className="rounded-full border border-slate-200 bg-slate-50 px-3 py-1 text-xs font-medium text-slate-600">
                    {formatDateRange(project.start_date, project.end_date)}
                </span>
            </div>

            {project.description && (
                <p className="mt-4 text-sm leading-6 text-slate-600">
                    {project.description}
                </p>
            )}

            <div className="mt-6 flex flex-wrap gap-4 text-sm text-slate-600">
                <span>{project.volunteer_count ?? 0} volunteers</span>
                <span>{project.materials?.length ?? 0} materials</span>
                <span>{project.sourcing_locations?.length ?? 0} sourcing spots</span>
            </div>

            <div className="mt-6">
                <p className="text-xs font-semibold uppercase tracking-wide text-slate-500">
                    Tools
                </p>
                <div className="mt-3 flex flex-wrap gap-3">
                    {tools.length === 0 && (
                        <span className="text-sm text-slate-400">No tools yet</span>
                    )}
                    {tools.slice(0, 4).map((tool) => {
                        const iconUrl = buildIconUrl(tool.svg_path);
                        return (
                            <div
                                key={tool.id ?? tool.name}
                                className="flex items-center gap-2 rounded-full border border-slate-200 bg-slate-50 px-3 py-1 text-xs text-slate-600"
                            >
                                {iconUrl ? (
                                    <img
                                        src={iconUrl}
                                        alt={tool.name}
                                        className="h-4 w-4"
                                    />
                                ) : (
                                    <span className="h-2 w-2 rounded-full bg-slate-300" />
                                )}
                                <span>{tool.name}</span>
                            </div>
                        );
                    })}
                </div>
            </div>
        </article>
    );
};

const App = () => {
    const { data, isLoading, isError } = useQuery({
        queryKey: ['projects'],
        queryFn: () => getProjects(),
    });

    const projects = data?.items ?? [];

    return (
        <div className="min-h-screen bg-gradient-to-br from-slate-50 via-white to-slate-100">
            <main className="mx-auto w-full max-w-6xl px-6 py-12">
                <header className="flex flex-wrap items-center justify-between gap-4">
                    <div>
                        <p className="text-xs font-semibold uppercase tracking-[0.2em] text-slate-500">
                            ArchiveKKN
                        </p>
                        <h1 className="mt-2 text-3xl font-semibold text-slate-900 sm:text-4xl">
                            Project dashboard
                        </h1>
                        <p className="mt-2 text-sm text-slate-600">
                            {isLoading
                                ? 'Loading projects from the API...'
                                : `${projects.length} projects available`}
                        </p>
                    </div>
                    <div className="rounded-full border border-slate-200 bg-white px-4 py-2 text-xs font-medium text-slate-600">
                        Connected to API
                    </div>
                </header>

                {isError && (
                    <div className="mt-10 rounded-2xl border border-rose-200 bg-rose-50 px-6 py-4 text-sm text-rose-700">
                        Unable to load projects. Make sure the backend API is running and CORS is enabled.
                    </div>
                )}

                {isLoading && !isError && (
                    <div className="mt-10 grid gap-6 sm:grid-cols-2">
                        {[...Array(4)].map((_, index) => (
                            <div
                                key={index}
                                className="h-48 animate-pulse rounded-2xl border border-slate-200 bg-white/70"
                            />
                        ))}
                    </div>
                )}

                {!isLoading && !isError && projects.length === 0 && (
                    <div className="mt-10 rounded-2xl border border-slate-200 bg-white px-6 py-4 text-sm text-slate-600">
                        No projects yet. Add data via Postman or the backend API.
                    </div>
                )}

                {!isLoading && !isError && projects.length > 0 && (
                    <div className="mt-10 grid gap-6 sm:grid-cols-2">
                        {projects.map((project) => (
                            <ProjectCard key={project.id} project={project} />
                        ))}
                    </div>
                )}
            </main>
        </div>
    );
};

export default App;
